# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.dblib.db_cloudfs_container import db_cloudfs_container_delete,db_cloudfs_container_put
from cloudweb.db.message.message_container import db_message_container_delete,db_message_container_put
from cloudweb.globalx.variable import GLOBAL_USER_DB 
from cloudweb.drive.consistency import db_consistent
from cloudweb.db.table.lock.mysql import getlock

@db_consistent
def cloudfsContainerDelete(req):
    param = json.loads(req.body)
    objPath = param.get('objPath')
    newPath = param.get('newPath')
    
    atName = newPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        db_message_container_delete(conn, objPath)
        db_cloudfs_container_delete(newPath, conn)    
    return jresponse('0','',req,200)

@db_consistent
def cloudfsContainerPut(req):
    
    param = json.loads(req.body)
    objPath = param.get('objPath')
    newPath = param.get('newPath')
    atName = newPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        db_cloudfs_container_put(newPath, conn)
        db_message_container_put(conn, objPath)
    return jresponse('0','',req,200)

################################################

def cloudfsContainerHead(req):
    return jresponse('0','',req,200)

def cloudfsContainerMeta(req):
    return jresponse('0','',req,200)


def cloudfsContainerPost(req):
    return jresponse('0','',req,200)

def cloudfsContainerGet(req):
    return jresponse('0','',req,200)
