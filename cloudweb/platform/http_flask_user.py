# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.events.events import Event
from cloudweb.events.restful.user import getToken

from cloudweb.db.db_user import user2attr
from cloudweb.dblib.db_flask_user import db_flask_user_delete,db_flask_user_disable,db_flask_user_enable,db_flask_user_list
from cloudweb.dblib.db_flask_account import db_flask_account_disable,db_flask_account_enable

def flaskUserLogin(req,sdata):

    param = json.loads(req.body)
    email = param.get('email')
    passwd = param.get('passwd')
    
    userName = 'AUTH_' + email.replace('@','').replace('.','') 
    resp = getToken(email,passwd)
    if '-1' == resp['status']:
        return jresponse(resp['status'],resp['msg'],req,200)
    
    ev = Event(email,passwd,sdata)
    tokendict = json.loads(resp['msg'])
    sdata.token.setToken(ev.getAtName(),tokendict.get('access_token'))
    sdata.user.setUser(ev.getAtName(),ev)
    
    attr = user2attr(ev.db, userName)
    tokendict.update(attr)
    resp['msg'] = json.dumps(tokendict)
    return jresponse(resp['status'],resp['msg'],req,200)

def flaskUserList(req,sdata):

    param = json.loads(req.body)
    atName = param.get('atName')
    ev = sdata.user.getUser(atName)
    
    metadata = db_flask_user_list(ev.db)
    
    return jresponse('0',json.dumps(metadata),req,200)

def flaskUserEnable(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    urName = param.get('urName')
    # check atName type ; only admin do
    
    ev = sdata.user.getUser(atName)
    db_flask_user_enable(ev.db, urName)
    db_flask_account_enable(ev.db, urName )
    
    return jresponse('0',json.dumps({}),req,200)

def flaskUserDisable(req,sdata):

    param = json.loads(req.body)
    atName = param.get('atName')
    urName = param.get('urName')

    ev = sdata.user.getUser(atName)
    db_flask_user_disable(ev.db,urName)
    db_flask_account_disable(ev.db, urName) 
    
    return jresponse('0',json.dumps({}),req,200)

def flaskUserDelete(req,sdata):

    param = json.loads(req.body)
    atName = param.get('atName')
    urName = param.get('urName')

    # check atName type ; only admin do
        
    ev = sdata.user.getUser(atName)
    db_flask_user_delete(ev.db, urName)
    db_flask_account_disable(ev.db,urName)    
    return jresponse('0',json.dumps({}),req,200)
