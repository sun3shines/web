# -*- coding: utf-8 -*-

from cloudweb.db.dynamic.db_service import query_service
from cloudweb.db.table.static.host import uuid2hostid

def db_flask_query_service(db,hostUuid):
        
    host_id = uuid2hostid(db, hostUuid)    
    return query_service(db, host_id)
