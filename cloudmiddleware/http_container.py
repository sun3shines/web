# -*- coding: utf-8 -*-

from urllib import unquote
from functools import wraps

import cloudmiddleware.mission as mission 
from cloudmiddleware.class_container import CloudfsContainerDelete,CloudfsContainerGet,CloudfsContainerHead,\
    CloudfsContainerMeta,CloudfsContainerPost,CloudfsContainerPut
from qpid.peer import Responder
    
def cloudfs_container_delete(func):
    
    @wraps(func)
    def wrapper(*args,**kwargs):
        resp = func(*args,**kwargs)
        if 2 != resp.status_int/100:
            return resp
        
        http_dict = resp.request.environ.get('http_dict')
        request_path = http_dict.get('request_path')
        path = unquote(request_path)
        newPath = '/'.join(path.split('/')[3:])
     
        objPath = unquote(request_path)
        objPath = '/'.join(objPath.split('/')[3:])    
        msgparam = {'objPath':objPath}
        
        t = CloudfsContainerDelete(newPath,msgparam)
        t = mission.execute(t)
        t.response
        return resp
    
    return wrapper

def cloudfs_container_put(func):
    
    @wraps(func)
    def wrapper(*args,**kwargs):

        resp = func(*args,**kwargs)
        if 2 != resp.status_int/100:
            return resp
        http_dict = resp.request.environ.get('http_dict')
        request_path = http_dict.get('request_path')
        path = unquote(request_path)
        newPath = '/'.join(path.split('/')[3:])
        
        objPath = unquote(request_path)
        objPath = '/'.join(objPath.split('/')[3:])    
        msgparam = {'objPath':objPath}
        
        t = CloudfsContainerPut(newPath,msgparam)
        t = mission.execute(t)
        t.response
        return resp
    
    return wrapper

###################################################

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

