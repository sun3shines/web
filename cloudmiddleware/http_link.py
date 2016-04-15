# -*- coding: utf-8 -*-

from urllib import unquote
from functools import wraps
import cloudmiddleware.mission as mission 
from cloudmiddleware.class_link import CloudfsLinkPut

def cloudfs_link_put(func):
    
    @wraps(func)
    def wrapper(*args,**kwargs):

        resp = func(*args,**kwargs)
        if 2 != resp.status_int/100:
            return resp
        http_dict = resp.request.environ.get('http_dict')
        request_path = http_dict.get('request_path')
        dstName = http_dict.get('dstName')
        srcName = http_dict.get('srcName')
        
        path = unquote(request_path)
        newPath = '/'.join(path.split('/')[3:])
        
        # objPath = unquote(srcName)
        # objPath = '/'.join(objPath.split('/')[3:])
        
        objPath = newPath
        msgparam = {'objPath':objPath,'dstName':dstName}
        
        t = CloudfsLinkPut(newPath,msgparam)
        t = mission.execute(t)
        t.response
        return resp
    return wrapper

