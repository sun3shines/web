# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.dblib.db_cloudfs_account import db_cloudfs_account_delete,db_cloudfs_account_put
from cloudweb.db.message.message_account import db_message_account_put,db_message_account_delete
from cloudweb.dblib.db_cloudfs_user import db_cloudfs_user_put
from cloudweb.globalx.variable import GLOBAL_USER_DB 

def cloudfsAccountPut(req):
    
    param = json.loads(req.body)
    newPath = param.get('newPath')
    objPath = param.get('objPath')
    
    atName = newPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    
    db_cloudfs_account_put(newPath, conn)
    db_cloudfs_user_put(conn, newPath)
    db_message_account_put(conn, objPath)
    
    return jresponse('0','',req,200)

########################################

def cloudfsAccountDelete(req):
    param = json.loads(req.body)
    newPath = param.get('newPath')
    objPath = param.get('objPath')
    
    atName = newPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    
    db_message_account_delete(conn, objPath)
    db_cloudfs_account_delete(newPath, conn)
    
    return jresponse('0','',req,200)

def cloudfsAccountGet(req):
    
    return jresponse('0','',req,200)

def cloudfsAccountPost(req):
    
    return jresponse('0','',req,200)

def cloudfsAccountHead(req):
    
    return jresponse('0','',req,200)

def cloudfsAccountMeta(req):
    
    return jresponse('0','',req,200)
