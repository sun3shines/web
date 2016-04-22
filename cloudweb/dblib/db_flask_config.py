# -*- coding: utf-8 -*-

from cloudweb.db.table.config.executor import ip2attrs,uuid2attrs,query_all_executor,\
    insert_executor,del_executor

def db_flask_ip2attr(db,hostip):
    return ip2attrs(db, hostip)

def db_flask_uuid2attr(db,uuid):
    return uuid2attrs(db, uuid)

def db_flask_list_executor(db):
    
    return query_all_executor(db)

def db_flask_put_executor(db,name,inet,uuid):
    return insert_executor(db, name, uuid, inet, 'enable')

def db_flask_del_executor(db,hostUuid):
    eid = uuid2attrs(db, hostUuid).get('id')
    return del_executor(db, eid)