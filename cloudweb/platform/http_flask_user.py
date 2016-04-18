# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.globalx.variable import GLOBAL_USER_TOKEN,GLOBAL_USER_DB
from cloudlib.restful.cloudfs.lib_token import libGetTokenAttr

from cloudweb.db.db_user import user2attr
from cloudweb.dblib.db_flask_user import db_flask_user_delete,db_flask_user_disable,db_flask_user_enable,db_flask_user_list
from cloudweb.dblib.db_flask_account import db_flask_account_disable,db_flask_account_enable

def flaskUserLogin(req,sdata):

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
    
    attr = user2attr(conn, userName)
    tokendict.update(attr)
    resp['msg'] = json.dumps(tokendict)
    return jresponse(resp['status'],resp['msg'],req,200)

def flaskUserList(req,sdata):

    param = json.loads(req.body)
    atName = param.get('atName')
    
    conn = GLOBAL_USER_DB.get(atName)
    metadata = db_flask_user_list(conn)
    
    return jresponse('0',json.dumps(metadata),req,200)

def flaskUserEnable(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    urName = param.get('urName')
    # check atName type ; only admin do
    
    conn = GLOBAL_USER_DB.get(atName)
    db_flask_user_enable(conn, urName)
    db_flask_account_enable(conn, urName )
    
    return jresponse('0',json.dumps({}),req,200)

def flaskUserDisable(req,sdata):

    param = json.loads(req.body)
    atName = param.get('atName')
    urName = param.get('urName')

    conn = GLOBAL_USER_DB.get(atName)
    db_flask_user_disable(conn,urName)
    db_flask_account_disable(conn, urName) 
    
    return jresponse('0',json.dumps({}),req,200)

def flaskUserDelete(req,sdata):

    param = json.loads(req.body)
    atName = param.get('atName')
    urName = param.get('urName')

    # check atName type ; only admin do
    
    conn = GLOBAL_USER_DB.get(atName)
    db_flask_user_delete(conn, urName)
    db_flask_account_disable(conn,urName)    
    return jresponse('0',json.dumps({}),req,200)
