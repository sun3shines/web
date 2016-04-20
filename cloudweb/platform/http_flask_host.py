# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.dblib.db_flask_static import db_flask_query_all_static
from cloudweb.globalx.variable import GLOBAL_USER_DB
from cloudweb.db.table.lock.mysql import getlock

def flaskQueryAllStatic(request,sdata):
    
    param = json.loads(request.body)
    atName = param.get('atName')
    conn = GLOBAL_USER_DB.get(atName)
    metadata = {}
    with getlock(conn) as mylock:
        metadata = db_flask_query_all_static(conn)
    return jresponse('0',json.dumps(metadata),request,200) 

def flaskQueryService(request,sdata):
    pass

def flaskQueryStatClass(request,sdata):
    pass

