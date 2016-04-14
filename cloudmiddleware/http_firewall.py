# -*- coding: utf-8 -*-

from urllib import unquote
import cloudmiddleware.mission as mission 

from cloudmiddleware.class_firewall import CloudfsAccountValid,CloudfsObjectValid

def cloudfs_account_valid(request_path):
    path = unquote(request_path)
    newPath = '/'.join(path.split('/')[3:])
    
    t = CloudfsAccountValid(newPath)
    t = mission.execute(t)
    return t.response

def cloudfs_object_valid(request_path):
 
    path = unquote(request_path)
    newPath = '/'.join(path.split('/')[3:])

    t = CloudfsObjectValid(newPath)
    t = mission.execute(t)
    return t.response
