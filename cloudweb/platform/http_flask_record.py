# -*- coding: utf-8 -*-

import json
import time
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.dblib.db_flask_record import db_flask_record_object,db_flask_record_user

def flaskGetObjectRecords(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    objPath = param.get('objPath')
    
    ev = sdata.user.getUser(atName)
    metadata = db_flask_record_object(ev.db, '/'.join([atName,objPath]))
   
    attrs = []
    for attr in metadata:
        attrs.append((attr[0],attr[1],str(attr[2])))
 
    return jresponse('0',json.dumps(attrs),req,200)

def flaskGetAccountRecords(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')

    ev = sdata.user.getUser(atName)
    metadata = db_flask_record_user(ev.db, atName)
    attrs = []
    for attr in metadata:
        attrs.append((attr[0],attr[1],str(attr[2])))
    return jresponse('0',json.dumps(attrs),req,200)

