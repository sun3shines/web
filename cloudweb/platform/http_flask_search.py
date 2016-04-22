# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.db.table.stobj import id2urlAttrs
from cloudweb.dblib.db_flask_search import db_flask_search_account_objects,db_flask_search_global_objects
from cloudweb.platform.globalx.variable import GLOBAL_USER_TOKEN,GLOBAL_USER_DB
from cloudlib.restful.cloudfs.lib_object import libGetObjectMeta
from cloudlib.restful.cloudfs.lib_container import libGetContainerMeta
from cloudlib.restful.cloudfs.lib_account import libGetAccountMeta
from cloudweb.platform.drive.consistency import flask_consistent
from cloudweb.db.table.lock.mysql import getlock

@flask_consistent
def flaskDataGlobalSearch(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    keyword = param.get('keyword')
    objects = []
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        objects = db_flask_search_global_objects(conn,keyword)
        objects = json.dumps(objects)
    return jresponse('0',objects,req,200)

@flask_consistent
def flaskDataUserSearch(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    keyword = param.get('keyword')
    objects = []
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        objects = db_flask_search_account_objects(conn,atName, keyword)
        objects = json.dumps(objects)
    return jresponse('0', objects, req,200) 

@flask_consistent
def flaskDataObjectDetail(req,sdata):

    param = json.loads(req.body)
    atName = param.get('atName')
    oid = param.get('objectId')
    
    usertoken = GLOBAL_USER_TOKEN.get_user_token(atName)
    conn = GLOBAL_USER_DB.get(atName)
    
    
    with getlock(conn) as mylock:
        flag,attr = id2urlAttrs(oid,conn)
    
    if not flag:
        return jresponse('-1','id2urlAttrs Error: '+str(oid),req,200)
    
    if 'account' == attr.get('type'):
        resp = libGetAccountMeta(atName, usertoken)
    elif 'container' == attr.get('type'):
        resp = libGetContainerMeta(atName, usertoken, attr['path'].replace(atName,'',1))
    else:
        resp = libGetObjectMeta(atName, usertoken, attr['path'].replace(atName,'',1))
        
    if '0' == resp['status']:
        msg = json.loads(resp['msg'])
        if 'account' == attr.get('type'):
            msg['urlPath'] = atName
        else:
            msg['urlPath'] = attr['path']
        keys = ['X-Container-Bytes-Used','X-Container-Object-Count','X-Versions-Location',
                'X-Account-Bytes-Used','X-Account-Meta-Quota-Bytes','X-File-Type',
                'X-Object-Permisson','ETag']
        for key in keys:
            if not msg.has_key(key):
                continue
            if key =='ETag':
                newkey = 'Md5'
            else:
                newkey = key[2:]
            msg[newkey] = msg[key]
            msg.pop(key)
        keys = ['X-PUT-Timestamp','X-Timestamp']
        for key in keys:
            if not msg.has_key(key):
                continue
            msg.pop(key)
        resp['msg'] = json.dumps(msg)
        
    return jresponse(resp['status'],resp['msg'],req,200)
