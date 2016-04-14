# -*- coding: utf-8 -*-

from urllib import unquote
import cloudmiddleware.mission as mission 
from cloudmiddleware.class_container import CloudfsContainerDelete,CloudfsContainerGet,CloudfsContainerHead,\
    CloudfsContainerMeta,CloudfsContainerPost,CloudfsContainerPut
    
def cloudfs_container_delete(request_path):
    
    path = unquote(request_path)
    newPath = '/'.join(path.split('/')[3:])
 
    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])    
    msgparam = {'objPath':objPath}
    
    t = CloudfsContainerDelete(newPath,msgparam)
    t = mission.execute(t)
    return t.response


def cloudfs_container_put(request_path):
    path = unquote(request_path)
    newPath = '/'.join(path.split('/')[3:])
    
    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])    
    msgparam = {'objPath':objPath}
    
    t = CloudfsContainerPut(newPath,msgparam)
    t = mission.execute(t)
    return t.response

def cloudfs_container_head(request_path):
    
    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])    
    msgparam = {'objPath':objPath}
    
    t = CloudfsContainerHead(msgparam)
    t = mission.execute(t)
    return t.response

def cloudfs_container_meta(request_path):

    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])    
    msgparam = {'objPath':objPath}
    
    t = CloudfsContainerMeta(msgparam)
    t = mission.execute(t)
    return t.response

def cloudfs_container_post(request_path,header):

    
    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])    
    msgparam = {'objPath':objPath,'header':header}
    
    t = CloudfsContainerPost(msgparam)
    t = mission.execute(t)
    return t.response

def cloudfs_container_get(request_path):
    
    
    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])    
    msgparam = {'objPath':objPath}
    
    t = CloudfsContainerGet(msgparam)
    t = mission.execute(t)
    return t.response

