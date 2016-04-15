# -*- coding: utf-8 -*-

from urllib import unquote
from functools import wraps
import cloudmiddleware.mission as mission 
from cloudmiddleware.class_account import CloudfsAccountPut,CloudfsAccountDelete,CloudfsAccountExists,\
    CloudfsAccountGet,CloudfsAccountHead,CloudfsAccountMeta,CloudfsAccountPost
    
def cloudfs_account_put(func):
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
        
        t = CloudfsAccountPut(newPath,msgparam)
        mission.execute(t)
        t.response
        return resp
    return wrapper

def cloudfs_account_delete(func):
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
    
        t = CloudfsAccountDelete(newPath)
        mission.execute(t)
        t.response
        return resp
    return wrapper

####################################################

def cloudfs_account_exists(request_path):
    
    path = unquote(request_path)
    newPath = '/'.join(path.split('/')[2])
    
    t = CloudfsAccountExists(newPath)
    mission.execute(t)
    return t.response    
    
def cloudfs_account_get(request_path):

    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])    
    msgparam = {'objPath':objPath}
    t = CloudfsAccountGet(msgparam)
    t = mission.execute(t)
    return t.response

def cloudfs_account_post(request_path):
    
    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])
    msgparam = {}

    t = CloudfsAccountPost(msgparam)
    t = mission.execute(t)
    return t.response

def cloudfs_account_head(request_path):

    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])    
    msgparam = {'objPath':objPath}
    t = CloudfsAccountHead(msgparam)
    t = mission.execute(t)
    return t.response

def cloudfs_account_meta(request_path):

    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])    
    msgparam = {'objPath':objPath}
    t = CloudfsAccountMeta(msgparam)
    t = mission.execute(t)
    return t.response

