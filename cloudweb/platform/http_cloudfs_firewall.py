# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.dblib.db_cloudfs_firewall import db_cloudfs_account_valid,db_cloudfs_object_valid
from cloudweb.globalx.variable import GLOBAL_USER_DB 
from cloudweb.drive.consistency import db_consistent

@db_consistent
def cloudfsAccountValid(req):
    param = json.loads(req.body)
    newPath = param.get('newPath')
    
    atName = newPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    
    db_cloudfs_account_valid(newPath, conn)    
    return jresponse('0','',req,200)

@db_consistent
def cloudfsObjectValid(req):
    
    param = json.loads(req.body)
    newPath = param.get('newPath')
    
    atName = newPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    
    db_cloudfs_object_valid(newPath, conn)    
    return jresponse('0','',req,200)
