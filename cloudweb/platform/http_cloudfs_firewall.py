# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.dblib.db_cloudfs_firewall import db_cloudfs_account_valid,db_cloudfs_object_valid
from cloudweb.platform.globalx.variable import GLOBAL_USER_DB 
from cloudweb.platform.drive.consistency import db_consistent
from cloudweb.db.table.lock.mysql import getlock

def cloudfsAccountValid(req):
    param = json.loads(req.body)
    newPath = param.get('newPath')
    
    atName = newPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        db_cloudfs_account_valid(newPath, conn)    
    return jresponse('0','',req,200)

def cloudfsObjectValid(req):
    
    param = json.loads(req.body)
    newPath = param.get('newPath')
    
    atName = newPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        db_cloudfs_object_valid(newPath, conn)    
    return jresponse('0','',req,200)
