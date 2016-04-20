# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse

from cloudweb.globalx.variable import GLOBAL_USER_DB
from cloudweb.db.table.lock.mysql import getlock
from cloudweb.dblib.db_flask_static import db_flask_query_all_static
from cloudweb.dblib.db_flask_dynamic import db_flask_query_dynamic_class
from cloudweb.dblib.db_flask_service import db_flask_query_service
from cloudweb.globalx.variable import strTimeStamp

def flaskQueryAllStatic(request,sdata):
    
    param = json.loads(request.body)
    atName = param.get('atName')
    conn = GLOBAL_USER_DB.get(atName)
    metadata = {}
    with getlock(conn) as mylock:
        metadata = db_flask_query_all_static(conn)
    return jresponse('0',json.dumps(metadata),request,200) 

def flaskQueryService(request,sdata):
    
    param = json.loads(request.body)
    atName = param.get('atName')
    hostUuid = param.get('hostUuid')
    conn = GLOBAL_USER_DB.get(atName)
    metadata = []
    with getlock(conn) as mylock:
        metadata = db_flask_query_service(conn, hostUuid)
        
    for attr in metadata:
        attr[strTimeStamp] = str(attr.pop(strTimeStamp))
        
    return jresponse('0',json.dumps(metadata),request,200) 


def flaskQueryStatClass(request,sdata):
    param = json.loads(request.body)
    atName = param.get('atName')
    hostUuid = param.get('hostUuid')
    className = param.get('className')
    
    conn = GLOBAL_USER_DB.get(atName)
    
    metadata = []
    with getlock(conn) as mylock:
        metadata = db_flask_query_dynamic_class(conn, hostUuid, className)
        
    for attr in metadata:
        attr[strTimeStamp] = str(attr.pop(strTimeStamp))
        
    return jresponse('0',json.dumps(metadata),request,200)

