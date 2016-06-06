# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.platform.globalx.variable import GLOBAL_USER_TOKEN,GLOBAL_USER_DB,GLOBAL_USER_CONSISTENCY,\
    GLOBAL_ADMIN_TOKENS
from cloudlib.restful.cloudfs.lib_token import libGetTokenAttr

from cloudweb.db.db_user import user2attr
from cloudweb.dblib.db_flask_user import db_flask_user_delete,db_flask_user_disable,\
    db_flask_user_enable,db_flask_user_list
from cloudweb.dblib.db_flask_account import db_flask_account_disable,db_flask_account_enable
from cloudweb.platform.drive.consistency import flask_consistent
from cloudweb.platform.tools.init_consistency_db import getDirList
from cloudweb.db.table.lock.mysql import getlock
from cloudweb.dblib.db_flask_user import db_flask_user_put
from cloudweb.db.table.user import User

def flaskUserLogin(req):
    param = json.loads(req.body)
    email = param.get('email')
    passwd = param.get('passwd')
    
    atName = userName = 'AUTH_' + email.replace('@','').replace('.','') 
    resp = libGetTokenAttr(email, passwd)
    
    if '-1' == resp['status']:
        return jresponse(resp['status'],resp['msg'],req,200)
    
    tokendict = json.loads(resp['msg'])
    conn = GLOBAL_USER_DB.get(atName)
    GLOBAL_USER_TOKEN.put(atName, email, passwd, tokendict.get('access_token'))
    
    if GLOBAL_USER_CONSISTENCY.failed(atName):
        with getlock(conn) as mylock:
            db_flask_user_put(conn, atName)
            flag,msg = getDirList(conn, atName, tokendict.get('access_token'), 0)
            if not flag:
                return jresponse('-1', msg, req, 400)
        GLOBAL_USER_CONSISTENCY.put(atName, GLOBAL_USER_CONSISTENCY.state_success)
    
    attr = user2attr(conn, userName)
    u = User()
    if str(attr.get(u.type)) == 'admin':
        GLOBAL_ADMIN_TOKENS.put(tokendict.get('access_token').lower())
    
    tokendict.update(attr)
    resp['msg'] = json.dumps(tokendict)
    return jresponse(resp['status'],resp['msg'],req,200)

@flask_consistent
def flaskUserList(req):

    param = json.loads(req.body)
    atName = param.get('atName').encode('utf-8')
    
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        metadata = db_flask_user_list(conn)
    
    return jresponse('0',json.dumps(metadata),req,200)

@flask_consistent
def flaskUserEnable(req):
    
    param = json.loads(req.body)
    atName = param.get('atName').encode('utf-8')
    urName = param.get('urName').encode('utf-8')
    # check atName type ; only admin do
    
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        db_flask_user_enable(conn, urName)
        db_flask_account_enable(conn, urName )
    
    return jresponse('0',json.dumps({}),req,200)

@flask_consistent
def flaskUserDisable(req):

    param = json.loads(req.body)
    atName = param.get('atName').encode('utf-8')
    urName = param.get('urName').encode('utf-8')
    
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        db_flask_user_disable(conn,urName)
        db_flask_account_disable(conn, urName) 
    
    return jresponse('0',json.dumps({}),req,200)

@flask_consistent
def flaskUserDelete(req):

    param = json.loads(req.body)
    atName = param.get('atName').encode('utf-8')
    urName = param.get('urName').encode('utf-8')

    # check atName type ; only admin do
    
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        db_flask_user_delete(conn, urName)
        db_flask_account_disable(conn,urName)    
    return jresponse('0',json.dumps({}),req,200)

