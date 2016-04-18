# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.dblib.db_cloudfs_dir import db_cloudfs_dir_delete,db_cloudfs_dir_reset,db_cloudfs_dir_deleterecycle,\
    db_cloudfs_dir_moverecycle,db_cloudfs_dir_put,db_cloudfs_dir_move,db_cloudfs_dir_copy
from cloudweb.db.message.message_dir import db_message_dir_delete,db_message_dir_reset,db_message_dir_deleterecycle,\
    db_message_dir_moverecycle,db_message_dir_put,db_message_dir_move,db_message_dir_copy
from cloudweb.globalx.variable import GLOBAL_USER_DB 
from cloudweb.drive.consistency import db_consistent

@db_consistent
def cloudfsDirPut(req):

    param = json.loads(req.body)
    objPath = param.get('objPath')
    newPath = param.get('newPath')
    atName = newPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    
    db_cloudfs_dir_put(newPath, conn)
    db_message_dir_put(conn, objPath)
    
    return jresponse('0','',req,200)

@db_consistent
def cloudfsDirDelete(req):
    
    param = json.loads(req.body)
    objPath = param.get('objPath')
    newPath = param.get('newPath')
    atName = newPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    
    
    db_message_dir_delete(conn, objPath)
    db_cloudfs_dir_delete(newPath, conn)
    
    return jresponse('0','',req,200)

def cloudfsDirReset(req):
    param = json.loads(req.body)
    objPath = param.get('objPath')
    newPath = param.get('newPath')
    atName = newPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    
    db_message_dir_reset(conn, objPath)
    db_cloudfs_dir_reset(newPath, conn)
    return jresponse('0','',req,200)

def cloudfsDirDeleteRecycle(req):
    param = json.loads(req.body)
    srcNewPath = param.get('srcNewPath')
    dstNewPath = param.get('dstNewPath')
    objPath = param.get('objPath')
    
    atName = srcNewPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    
    db_message_dir_deleterecycle(conn, objPath)
    db_cloudfs_dir_deleterecycle(srcNewPath, dstNewPath, conn)
    return jresponse('0','',req,200)

def cloudfsDirMoveRecycle(req):
    param = json.loads(req.body)
    srcNewPath = param.get('srcNewPath')
    dstNewPath = param.get('dstNewPath')
    objPath = param.get('objPath')

    atName = srcNewPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    
    db_message_dir_moverecycle(conn, objPath)
    db_cloudfs_dir_moverecycle(srcNewPath, dstNewPath, conn)
    
    return jresponse('0','',req,200)

def cloudfsDirMove(req):
    param = json.loads(req.body)
    srcNewPath = param.get('srcNewPath')
    dstNewPath = param.get('dstNewPath')
    objPath = param.get('objPath')
    dstName = param.get('dstName')

    atName = srcNewPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    
    db_message_dir_move(conn, objPath, dstName)    
    db_cloudfs_dir_move(srcNewPath, dstNewPath, conn)
    
    return jresponse('0','',req,200)

def cloudfsDirCopy(req):
    param = json.loads(req.body)
    srcNewPath = param.get('srcNewPath')
    dstNewPath = param.get('dstNewPath')
    objPath = param.get('objPath')
    dstName = param.get('dstName')

    atName = srcNewPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    
    db_cloudfs_dir_copy(srcNewPath, dstNewPath, conn)
    db_message_dir_copy(conn, objPath, dstName)
    
    return jresponse('0','',req,200)

####################################################

def cloudfsDirMetaGet(req):
    return jresponse('0','',req,200)

def cloudfsDirGet(req):
    return jresponse('0','',req,200)
