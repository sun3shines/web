# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.db.table.stobj import id2urlAttrs
from cloudweb.dblib.db_flask_search import db_flask_search_account_objects,db_flask_search_global_objects
from cloudweb.events.restful.fs import getAccountMeta,getContainerMeta,getObjectMeta


def flaskDataGlobalSearch(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    keyword = param.get('keyword')
    
    ev = sdata.user.getUser(atName)
    objects = db_flask_search_global_objects(ev.db,keyword)
    objects = json.dumps(objects)
    return jresponse('0',objects,req,200)

def flaskDataUserSearch(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    keyword = param.get('keyword')
    
    ev = sdata.user.getUser(atName)
    
    objects = db_flask_search_account_objects(ev.db,atName, keyword)
    objects = json.dumps(objects)
    return jresponse('0', objects, req,200) 

def flaskDataObjectDetail(req,sdata):

    param = json.loads(req.body)
    atName = param.get('atName')
    oid = param.get('objectId')
    
    
    ev = sdata.user.getUser(atName)
    attr = id2urlAttrs(oid,ev.db)
    
    if 'account' == attr.get('type'):
        resp = getAccountMeta(ev)
    elif 'container' == attr.get('type'):
        resp = getContainerMeta(attr['path'].replace(atName,'',1), ev)   
    else:
        resp = getObjectMeta(attr['path'].replace(atName,'',1), ev)
        
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
