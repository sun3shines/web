# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.globalx.variable import GLOBAL_USER_DB
from cloudweb.globalx.static import CONFIG_EXECUTOR_PORT
from cloudweb.db.table.lock.mysql import getlock
from cloudweb.dblib.db_flask_config import db_flask_ip2attr,db_flask_list_executor,\
    db_flask_uuid2attr,db_flask_put_executor,db_flask_del_executor
from cloudlib.restful.config.lib_config import libPullExecutor

def flaskAddExecutor(request,sdata):
    
    param = json.loads(request.body)
    hostip = param.get('hostip')
    atName = param.get('atName')
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        attr = db_flask_ip2attr(conn, hostip)
    if not attr:
        info = '%s %s %s' % (attr.get('name'),attr.get('uuid'))
        return jresponse('-1','executor ip already exists: '+info,request,200) 
    resp = libPullExecutor(hostip, CONFIG_EXECUTOR_PORT)
    if -1 == resp['status']:
        return jresponse('-1','pull executor host info failed,check network',request,200)
    ei = resp.get('msg')
    with getlock(conn) as mylock:
        attr = db_flask_uuid2attr(conn, ei.get('uuid'))
        if attr:
            info = '%s %s %s' % (attr.get('name'),attr.get('uuid'),attr.get('ip'))
            return jresponse('-1','executor uuid already exists: '+info,request,200) 
        db_flask_put_executor(conn, ei.get('name'), ei.get('inet'), ei.get('uuid'))
    return jresponse('0','',request,200) 

def flaskDelExecutor(request,sdata):
    param = json.loads(request.body)
    hostUuid = param.get('hostUuid')
    atName = param.get('atName')
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        db_flask_del_executor(conn, hostUuid)
        
    return jresponse('0','',request,200) 

def flaskListExecutor(request,sdata):
    param = json.loads(request.body)
    atName = param.get('atName')
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        attrs = db_flask_list_executor(conn)
        for attr in attrs:
            attr.pop('id')
            
    return jresponse('0',json.dumps(attrs),request,200) 

def flaskSetConfig(request,sdata):
    return jresponse('0','',request,200) 

def flaskGetConfig(request,sdata):
    return jresponse('0','',request,200) 

