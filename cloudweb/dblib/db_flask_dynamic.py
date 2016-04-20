# -*- coding: utf-8 -*-

from cloudweb.db.dynamic.db_dynamic import query_stat_cpu,query_stat_disk,\
    query_stat_mem,query_stat_net,query_stat_storage
from cloudweb.db.table.static.host import uuid2hostid

stat_dict = {'cpu':query_stat_cpu,
             'disk':query_stat_disk,
             'net':query_stat_net,
             'mem':query_stat_mem,
             'storage':query_stat_storage}

def db_flask_query_dynamic_class(db,hostUuid,className):
        
    host_id = uuid2hostid(db, hostUuid)
    
    if stat_dict.has_key(className):
        return stat_dict[className](db,host_id)
    
    return []


