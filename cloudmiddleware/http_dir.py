# -*- coding: utf-8 -*-

from urllib import unquote
import cloudmiddleware.mission as mission 
from cloudmiddleware.class_dir import CloudfsDirCopy,CloudfsDirDelete,CloudfsDirDeleteRecycle,CloudfsDirGet,\
    CloudfsDirMetaGet,CloudfsDirMove,CloudfsDirMoveRecycle,CloudfsDirPut,CloudfsDirReset
    
def cloudfs_dir_delete(request_path):
    
    path = unquote(request_path)
    newPath = '/'.join(path.split('/')[3:])

    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])
    msgparam = {'objPath':objPath}
    
    t = CloudfsDirDelete(newPath,msgparam)
    t = mission.execute(t)
    return t.response

def cloudfs_dir_put(request_path):
    path = unquote(request_path)
    newPath = '/'.join(path.split('/')[3:])

    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])
    msgparam = {'objPath':objPath}
        
    t = CloudfsDirPut(newPath,msgparam)
    t = mission.execute(t)
    return t.response

def cloudfs_dir_reset(request_path):
    path = unquote(request_path)
    newPath = '/'.join(path.split('/')[3:])

    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])
    msgparam = {'objPath':objPath}
        
    t = CloudfsDirReset(newPath,msgparam)
    t = mission.execute(t)
    return t.response

def cloudfs_dir_deleterecycle(srcNewPath,dstNewPath,request_path):
    srcNewPath = unquote(srcNewPath)
    dstNewPath = unquote(dstNewPath)

    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])
    msgparam = {'objPath':objPath}
    
    t = CloudfsDirDeleteRecycle(srcNewPath,dstNewPath,msgparam)
    t = mission.execute(t)
    return t.response

def cloudfs_dir_moverecycle(srcNewPath,dstNewPath,request_path):
    
    srcNewPath = unquote(srcNewPath)
    dstNewPath = unquote(dstNewPath)

    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])
    msgparam = {'objPath':objPath}
    
    t = CloudfsDirMoveRecycle(srcNewPath,dstNewPath,msgparam)
    t = mission.execute(t)
    return t.response

def cloudfs_dir_move(srcNewPath,dstNewPath,request_path,dstName):
    srcNewPath = unquote(srcNewPath)
    dstNewPath = unquote(dstNewPath)
    
    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])
    msgparam = {'objPath':objPath,'dstName':dstName}
    t = CloudfsDirMove(srcNewPath,dstNewPath,msgparam)
    t = mission.execute(t)
    return t.response

def cloudfs_dir_copy(srcNewPath,dstNewPath,request_path,dstName):
    
    srcNewPath = unquote(srcNewPath)
    dstNewPath = unquote(dstNewPath)
    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])
    msgparam = {'objPath':objPath,'dstName':dstName}
    t = CloudfsDirCopy(srcNewPath,dstNewPath,msgparam)
    t = mission.execute(t)
    return t.response

def cloudfs_dir_metaget(request_path):
    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])
    msgparam = {'objPath':objPath}
        
    t = CloudfsDirMetaGet(msgparam)
    t = mission.execute(t)
    return t.response

def cloudfs_dir_get(request_path):

    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])
    msgparam = {'objPath':objPath}
        
    t = CloudfsDirGet(msgparam)
    t = mission.execute(t)
    return t.response

