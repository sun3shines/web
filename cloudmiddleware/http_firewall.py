# -*- coding: utf-8 -*-

from urllib import unquote
from functools import wraps
import cloudmiddleware.mission as mission 
from cloudlib.common.bufferedhttp import jresponse
from cloudmiddleware.class_firewall import CloudfsAccountValid,CloudfsObjectValid

def cloudfs_account_valid(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        request = args[1]
        http_dict = request.environ.get('http_dict')
        request_path = http_dict.get('request_path')
        path = unquote(request_path)
        newPath = '/'.join(path.split('/')[3:])
        
        t = CloudfsAccountValid(newPath)
        t = mission.execute(t)
        t.response
        if False:
            return jresponse('-1','account state invalid',request,403)
        
        return func(*args,**kwargs) 
    return wrapper 

def cloudfs_object_valid(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        request = args[1]
        http_dict = request.environ.get('http_dict')
        request_path = http_dict.get('request_path')
        path = unquote(request_path)
        newPath = '/'.join(path.split('/')[3:])
    
        t = CloudfsObjectValid(newPath)
        t = mission.execute(t)
        t.response
        if False:
            return jresponse('-1','object state invalid',request,403)
        
        return func(*args,**kwargs)  
    return wrapper 

