# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.dblib.db_cloudfs_firewall import db_cloudfs_account_valid,db_cloudfs_object_valid

def cloudfsAccountValid(req):
    param = json.loads(req.body)
    newPath = param.get('newPath')
    
    conn = None
    db_cloudfs_account_valid(newPath, conn)    
    return jresponse('0','',req,200)

def cloudfsObjectValid(req):
    
    param = json.loads(req.body)
    newPath = param.get('newPath')
    
    conn = None
    db_cloudfs_object_valid(newPath, conn)    
    return jresponse('0','',req,200)