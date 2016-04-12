# -*- coding: utf-8 -*-

import json
import time
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.db.record import getObjRecord,getUserRecord

def getObjectRecords(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    objPath = param.get('objPath')
    
    ev = sdata.user.getUser(atName)
    metadata = getObjRecord(ev.db, '/'.join([atName,objPath]))
   
    attrs = []
    for attr in metadata:
        attrs.append((attr[0],attr[1],str(attr[2])))
 
    return jresponse('0',json.dumps(attrs),req,200)

def getAccountRecords(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')

    ev = sdata.user.getUser(atName)
    metadata = getUserRecord(ev.db, atName)
    attrs = []
    for attr in metadata:
        attrs.append((attr[0],attr[1],str(attr[2])))
    return jresponse('0',json.dumps(attrs),req,200)

