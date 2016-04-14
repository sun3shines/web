# -*- coding: utf-8 -*-

import cloudmiddleware.mission as mission 
from urllib import unquote
from functools import wraps
from cloudmiddleware.class_object import CloudfsObjectCopy,CloudfsObjectDelete,CloudfsObjectDeleteRecycle,\
    CloudfsObjectGet,CloudfsObjectHead,CloudfsObjectMeta,CloudfsObjectMove,CloudfsObjectMoveRecycle,\
    CloudfsObjectPost,CloudfsObjectPut
    
def cloudfs_object_put(func):
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
        
        t = CloudfsObjectPut(newPath,msgparam)
        t = mission.execute(t)
        t.response
        return resp 
    return wrapper 

def cloudfs_object_delete(func):

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
        
        t = CloudfsObjectDelete(newPath,msgparam)
        t = mission.execute(t)
        t.response
        return resp 
    return wrapper 

def cloudfs_object_deleterecycle(func):

    @wraps(func)
    def wrapper(*args,**kwargs):

        resp = func(*args,**kwargs)
        if 2 != resp.status_int/100:
            return resp
        http_dict = resp.request.environ.get('http_dict')
        srcNewPath = http_dict.get('srcNewPath')
        dstNewPath = http_dict.get('dstNewPath')
        request_path = http_dict.get('request_path')
        srcNewPath = unquote(srcNewPath)
        dstNewPath = unquote(dstNewPath)
    
        objPath = unquote(request_path)
        objPath = '/'.join(objPath.split('/')[3:])
        msgparam = {'objPath':objPath}
        
        t = CloudfsObjectDeleteRecycle(srcNewPath,dstNewPath,msgparam)
        t = mission.execute(t)
        t.response
        return resp 
    return wrapper 

def cloudfs_object_copy(func):

    @wraps(func)
    def wrapper(*args,**kwargs):

        resp = func(*args,**kwargs)
        if 2 != resp.status_int/100:
            return resp
        http_dict = resp.request.environ.get('http_dict')   
        srcNewPath = http_dict.get('srcNewPath')
        dstNewPath = http_dict.get('dstNewPath')
        request_path = http_dict.get('request_path')
        dstName = http_dict.get('dstName') 
        srcNewPath = unquote(srcNewPath)
        dstNewPath = unquote(dstNewPath)
    
        objPath = unquote(request_path)
        objPath = '/'.join(objPath.split('/')[3:])
        msgparam = {'objPath':objPath,'dstName':dstName}
        
        t = CloudfsObjectCopy(srcNewPath,dstNewPath,msgparam)
        t = mission.execute(t)
        t.response
        return resp 
    return wrapper 

def cloudfs_object_move(func):

    @wraps(func)
    def wrapper(*args,**kwargs):

        resp = func(*args,**kwargs)
        if 2 != resp.status_int/100:
            return resp
        http_dict = resp.request.environ.get('http_dict')
        srcNewPath = http_dict.get('srcNewPath')
        dstNewPath = http_dict.get('dstNewPath')
        request_path = http_dict.get('request_path')
        dstName = http_dict.get('dstName') 
                
        srcNewPath = unquote(srcNewPath)
        dstNewPath = unquote(dstNewPath)
    
        objPath = unquote(request_path)
        objPath = '/'.join(objPath.split('/')[3:])
        msgparam = {'objPath':objPath,'dstName':dstName}
        
        t = CloudfsObjectMove(srcNewPath,dstNewPath,msgparam)
        t = mission.execute(t)
        t.response
        return resp
    return wrapper

def cloudfs_object_moverecycle(func):

    @wraps(func)
    def wrapper(*args,**kwargs):

        resp = func(*args,**kwargs)
        if 2 != resp.status_int/100:
            return resp
        http_dict = resp.request.environ.get('http_dict')
        srcNewPath = http_dict.get('srcNewPath')
        dstNewPath = http_dict.get('dstNewPath')
        request_path = http_dict.get('request_path')
        
        srcNewPath = unquote(srcNewPath)
        dstNewPath = unquote(dstNewPath)
        
        objPath = unquote(request_path)
        objPath = '/'.join(objPath.split('/')[3:])
        msgparam = {'objPath':objPath}
        
        t = CloudfsObjectMoveRecycle(srcNewPath,dstNewPath,msgparam)
        t = mission.execute(t)
        t.response
        return resp 
    return wrapper 

###################################################

def cloudfs_object_get(request_path):
    
    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])
    msgparam = {'objPath':objPath}
    t = CloudfsObjectGet(msgparam)
    t = mission.execute(t)
    return t.response

def cloudfs_object_head(request_path):

    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])
    msgparam = {'objPath':objPath}
    t = CloudfsObjectHead(msgparam)
    t = mission.execute(t)
    return t.response

def cloudfs_object_meta(request_path):

    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])
    msgparam = {'objPath':objPath}
    t = CloudfsObjectMeta(msgparam)
    t = mission.execute(t)
    return t.response

def cloudfs_object_post(request_path,header):

    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])
    msgparam = {'objPath':objPath,'header':header}
    t = CloudfsObjectPost(msgparam)
    t = mission.execute(t)
    return t.response

