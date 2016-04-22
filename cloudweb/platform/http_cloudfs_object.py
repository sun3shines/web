# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.dblib.db_cloudfs_object import db_cloudfs_object_put,db_cloudfs_object_delete,db_cloudfs_object_deleterecycle,\
    db_cloudfs_object_copy,db_cloudfs_object_move,db_cloudfs_object_moverecycle
from cloudweb.db.message.message_object import db_message_object_put,db_message_object_delete,db_message_object_deleterecycle,\
    db_message_object_copy,db_message_object_move,db_message_object_moverecycle
from cloudweb.platform.globalx.variable import GLOBAL_USER_DB 
from cloudweb.platform.drive.consistency import db_consistent
from cloudweb.db.table.lock.mysql import getlock

@db_consistent
def cloudfsObjectPut(req):
    
    param = json.loads(req.body)
    newPath = param.get('newPath')
    objPath = param.get('objPath')
    atName = newPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        db_cloudfs_object_put(newPath, conn)
        db_message_object_put(conn, objPath)
    
    return jresponse('0','',req,200)

@db_consistent
def cloudfsObjectDelete(req):
    
    param = json.loads(req.body)
    newPath = param.get('newPath')
    objPath = param.get('objPath')

    atName = newPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        db_message_object_delete(conn, objPath)
        db_cloudfs_object_delete(newPath, conn)
    return jresponse('0','',req,200)

@db_consistent
def cloudfsObjectDeleteRecycle(req):
    
    param = json.loads(req.body)
    objPath = param.get('objPath')
    srcNewPath = param.get('srcNewPath')
    dstNewPath = param.get('dstNewPath')
    
    atName = srcNewPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        db_message_object_deleterecycle(conn, objPath)
        db_cloudfs_object_deleterecycle(srcNewPath, dstNewPath, conn)
    return jresponse('0','',req,200)

@db_consistent
def cloudfsObjectCopy(req):
    
    param = json.loads(req.body)
    srcNewPath = param.get('srcNewPath')
    dstNewPath = param.get('dstNewPath')
    objPath = param.get('objPath')
    dstName = param.get('dstName')

    atName = srcNewPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        db_cloudfs_object_copy(srcNewPath, dstNewPath, conn)
        db_message_object_copy(conn, objPath, dstName)
    
    return jresponse('0','',req,200)

@db_consistent
def cloudfsObjectMove(req):
    
    param = json.loads(req.body)
    srcNewPath = param.get('srcNewPath')
    dstNewPath = param.get('dstNewPath')
    objPath = param.get('objPath')
    dstName = param.get('dstName')

    atName = srcNewPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        db_message_object_move(conn, objPath, dstName)
        db_cloudfs_object_move(srcNewPath, dstNewPath, conn)
    
    return jresponse('0','',req,200)

@db_consistent
def cloudfsObjectMoveRecycle(req):
    
    param = json.loads(req.body)
    objPath = param.get('objPath')
    srcNewPath = param.get('srcNewPath')
    dstNewPath = param.get('dstNewPath')

    atName = srcNewPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        db_message_object_moverecycle(conn, objPath)
        db_cloudfs_object_moverecycle(srcNewPath, dstNewPath, conn)
    return jresponse('0','',req,200)

##################################################

def cloudfsObjectGet(req):
    return jresponse('0','',req,200)

def cloudfsObjectHead(req):
    return jresponse('0','',req,200)

def cloudfsObjectMeta(req):
    return jresponse('0','',req,200)

def cloudfsObjectPost(req):
    return jresponse('0','',req,200)
