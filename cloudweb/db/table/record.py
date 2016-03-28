# -*- coding: utf-8 -*-

import datetime

class Record:
    def __init__(self):
        
        self.table = 'record'
        self.id = 'id'
        self.msg = 'msg'
        self.time = 'time'
        self.uid = 'uid'
        self.oid = 'oid'
        
def insert_record(db,msg,uid,oid):
    
    r = Record()
    keys = [r.msg,r.time,r.uid,r.oid]
    vals = [msg,str(datetime.datetime.now()),uid,oid]
    return db.insert(keys,vals,r.table)

def getRecords(db,uid='',oid=''):
    
    r = Record()
    attrs = [r.id,r.msg,r.time]
    c = {}
    if uid:
        c.update({r.uid:uid})
    if oid:
        c.update({r.oid:oid})
         
    return db.select(attrs,r.table,c)
