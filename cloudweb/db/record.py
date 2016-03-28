# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.table.user import name2id
from cloudweb.db.table.stobj import fullPath2id
from cloudweb.db.table.record import insert_record,getRecords

def rdPut(db,msg,urName,objPath):

    uid = name2id(db, urName)
    oid = fullPath2id(db, objPath)
    msg = msg.replace('AUTH_','')
    return insert_record(db, msg,uid, oid)

def getUserRecord(db,urName):
    
    uid = name2id(db,urName)
    return getRecords(db, uid=uid)

def getObjRecord(db,objPath):
    
    oid = fullPath2id(db,objPath)
    return getRecords(db, oid=oid)
