# -*- coding: utf-8 -*-

import json
import time
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.dblib.db_flask_record import db_flask_record_object,db_flask_record_user
from cloudweb.globalx.variable import GLOBAL_USER_DB
from cloudweb.drive.consistency import flask_consistent
from cloudweb.db.table.lock.mysql import getlock

@flask_consistent
def flaskGetObjectRecords(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    objPath = param.get('objPath')
    
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        metadata = db_flask_record_object(conn, '/'.join([atName,objPath]))
   
    attrs = []
    for attr in metadata:
        attrs.append((attr[0],attr[1],str(attr[2])))
 
    return jresponse('0',json.dumps(attrs),req,200)

@flask_consistent
def flaskGetAccountRecords(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')

    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        metadata = db_flask_record_user(conn, atName)
    attrs = []
    for attr in metadata:
        attrs.append((attr[0],attr[1],str(attr[2])))
    return jresponse('0',json.dumps(attrs),req,200)

