# -*- coding: utf-8 -*-

from urllib import unquote
import cloudmiddleware.mission as mission 
from cloudmiddleware.class_account import CloudfsAccountPut,CloudfsAccountDelete,CloudfsAccountExists,\
    CloudfsAccountGet,CloudfsAccountHead,CloudfsAccountMeta,CloudfsAccountPost
    
def cloudfs_account_put(request_path):
    
    path = unquote(request_path)
    newPath = '/'.join(path.split('/')[3:])
    
    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])
    msgparam = {'objPath':objPath}
    
    t = CloudfsAccountPut(newPath,msgparam)
    mission.execute(t)
    return t.response
    
def cloudfs_account_delete(request_path):

    path = unquote(request_path)
    newPath = '/'.join(path.split('/')[3:])

    # objPath = unquote(request_path)
    # objPath = '/'.join(objPath.split('/')[3:])    
    # msgparam = {}
    
    t = CloudfsAccountDelete(newPath)
    mission.execute(t)
    return t.response

def cloudfs_account_exists(request_path):
    
    path = unquote(request_path)
    newPath = '/'.join(path.split('/')[2])
    
    # msgparam = {}
    
    t = CloudfsAccountExists(newPath)
    mission.execute(t)
    return t.response    
    

####################################################

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

