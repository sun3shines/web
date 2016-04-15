# -*- coding: utf-8 -*-

from urllib import unquote
from functools import wraps

import cloudmiddleware.mission as mission 
from cloudmiddleware.class_dir import CloudfsDirCopy,CloudfsDirDelete,CloudfsDirDeleteRecycle,CloudfsDirGet,\
    CloudfsDirMetaGet,CloudfsDirMove,CloudfsDirMoveRecycle,CloudfsDirPut,CloudfsDirReset
    
def cloudfs_dir_delete(func):
    
    @wraps(func)
    def wrapper(*args,**kwargs):

        resp = func(*args,**kwargs)
        if 2 != resp.status_int/100:
            return resp
        for http_dict in[resp.request.environ.get('http_dict',{}),
                         resp.request.environ.get('http_version_dict',{})]:
            if not http_dict:
                continue
            request_path = http_dict.get('request_path')
            path = unquote(request_path)
            newPath = '/'.join(path.split('/')[3:])
        
            objPath = unquote(request_path)
            objPath = '/'.join(objPath.split('/')[3:])
            msgparam = {'objPath':objPath}
            
            t = CloudfsDirDelete(newPath,msgparam)
            t = mission.execute(t)
            t.response
        return resp
    return wrapper

def cloudfs_dir_put(func):

    @wraps(func)
    def wrapper(*args,**kwargs):

        resp = func(*args,**kwargs)
        if 2 != resp.status_int/100:
            return resp
        http_dict = resp.request.environ.get('http_dict')
        if not http_dict:
            return resp

        request_path = http_dict.get('request_path')
        path = unquote(request_path)
        newPath = '/'.join(path.split('/')[3:])
    
        objPath = unquote(request_path)
        objPath = '/'.join(objPath.split('/')[3:])
        msgparam = {'objPath':objPath}
            
        t = CloudfsDirPut(newPath,msgparam)
        t = mission.execute(t)
        t.response
        return resp
    return wrapper

def cloudfs_dir_reset(func):
    
    @wraps(func)
    def wrapper(*args,**kwargs):

        resp = func(*args,**kwargs)
        if 2 != resp.status_int/100:
            return resp
        for http_dict in[resp.request.environ.get('http_dict',{}),
                         resp.request.environ.get('http_version_dict',{})]:
            if not http_dict:
                continue
            request_path = http_dict.get('request_path')
            path = unquote(request_path)
            newPath = '/'.join(path.split('/')[3:])
        
            objPath = unquote(request_path)
            objPath = '/'.join(objPath.split('/')[3:])
            msgparam = {'objPath':objPath}
                
            t = CloudfsDirReset(newPath,msgparam)
            t = mission.execute(t)
            t.response
        return resp
    return wrapper

def cloudfs_dir_deleterecycle(func):

    @wraps(func)
    def wrapper(*args,**kwargs):

        resp = func(*args,**kwargs)
        if 2 != resp.status_int/100:
            return resp
        http_dict = resp.request.environ.get('http_dict')
        if not http_dict:
            return resp

        request_path = http_dict.get('request_path')
        srcNewPath = http_dict.get('srcNewPath')
        dstNewPath = http_dict.get('dstNewPath')
        
        srcNewPath = unquote(srcNewPath)
        dstNewPath = unquote(dstNewPath)
    
        objPath = unquote(request_path)
        objPath = '/'.join(objPath.split('/')[3:])
        msgparam = {'objPath':objPath}
        
        t = CloudfsDirDeleteRecycle(srcNewPath,dstNewPath,msgparam)
        t = mission.execute(t)
        t.response
        return resp
    return wrapper

def cloudfs_dir_moverecycle(func):

    @wraps(func)
    def wrapper(*args,**kwargs):

        resp = func(*args,**kwargs)
        if 2 != resp.status_int/100:
            return resp
        http_dict = resp.request.environ.get('http_dict')
        if not http_dict:
            return resp

        request_path = http_dict.get('request_path')
        srcNewPath = http_dict.get('srcNewPath')
        dstNewPath = http_dict.get('dstNewPath')
                   
        srcNewPath = unquote(srcNewPath)
        dstNewPath = unquote(dstNewPath)
    
        objPath = unquote(request_path)
        objPath = '/'.join(objPath.split('/')[3:])
        msgparam = {'objPath':objPath}
        
        t = CloudfsDirMoveRecycle(srcNewPath,dstNewPath,msgparam)
        t = mission.execute(t)
        t.response
        return resp
    return wrapper

def cloudfs_dir_move(func):
    @wraps(func)
    def wrapper(*args,**kwargs):

        resp = func(*args,**kwargs)
        if 2 != resp.status_int/100:
            return resp
        for http_dict in[resp.request.environ.get('http_dict',{}),
                         resp.request.environ.get('http_version_dict',{})]:
            if not http_dict:
                continue
            request_path = http_dict.get('request_path')
            srcNewPath = http_dict.get('srcNewPath')
            dstNewPath = http_dict.get('dstNewPath')
            dstName = http_dict.get('dstName')
            
            srcNewPath = unquote(srcNewPath)
            dstNewPath = unquote(dstNewPath)
            
            objPath = unquote(request_path)
            objPath = '/'.join(objPath.split('/')[3:])
            msgparam = {'objPath':objPath,'dstName':dstName}
            t = CloudfsDirMove(srcNewPath,dstNewPath,msgparam)
            t = mission.execute(t)
            t.response
        return resp
    return wrapper

def cloudfs_dir_copy(func):
    
    @wraps(func)
    def wrapper(*args,**kwargs):

        resp = func(*args,**kwargs)
        if 2 != resp.status_int/100:
            return resp
        for http_dict in[resp.request.environ.get('http_dict',{}),
                         resp.request.environ.get('http_version_dict',{})]:
            if not http_dict:
                continue
            request_path = http_dict.get('request_path')
            srcNewPath = http_dict.get('srcNewPath')
            dstNewPath = http_dict.get('dstNewPath')
            dstName = http_dict.get('dstName')
            
            srcNewPath = unquote(srcNewPath)
            dstNewPath = unquote(dstNewPath)
            objPath = unquote(request_path)
            objPath = '/'.join(objPath.split('/')[3:])
            msgparam = {'objPath':objPath,'dstName':dstName}
            t = CloudfsDirCopy(srcNewPath,dstNewPath,msgparam)
            t = mission.execute(t)
            t.response
        return resp
    return wrapper

###################################################

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

