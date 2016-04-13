# -*- coding: utf-8 -*-

from cloudweb.db.table.user import name2id
from cloudweb.db.table.stobj import fullPath2id
from cloudweb.db.table.record import insert_record

def record_put(db,msg,urName,objPath):

    uid = name2id(db, urName)
    oid = fullPath2id(db, objPath)
    msg = msg.replace('AUTH_','')
    return insert_record(db, msg,uid, oid)
