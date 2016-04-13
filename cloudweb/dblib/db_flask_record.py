# -*- coding: utf-8 -*-

from cloudweb.db.table.user import name2id
from cloudweb.db.table.stobj import fullPath2id
from cloudweb.db.table.record import getRecords

def db_flask_record_user(db,urName):
    
    uid = name2id(db,urName)
    return getRecords(db, uid=uid)

def db_flask_record_object(db,objPath):
    
    oid = fullPath2id(db,objPath)
    return getRecords(db, oid=oid)

