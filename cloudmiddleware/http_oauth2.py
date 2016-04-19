# -*- coding: utf-8 -*-

from urllib import unquote
from functools import wraps
import cloudmiddleware.mission as mission 
from cloudmiddleware.class_oauth2 import OauthRegister

def cloudfs_link_put(func):
    
    @wraps(func)
    def wrapper(*args,**kwargs):

        resp = func(*args,**kwargs)
        if 2 != resp.status_int/100:
            return resp
        
        http_dict = resp.request.environ.get('http_dict')
        if not http_dict:
            return resp

        email = http_dict.get('email')
        passwd = http_dict.get('passwd')
        usertoken = http_dict.get('usertoken')
         
        t = OauthRegister(email,passwd,usertoken)
        t = mission.execute(t)
        t.response
        return resp
    return wrapper

