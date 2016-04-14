# -*- coding: utf-8 -*-

from urllib import unquote
import cloudmiddleware.mission as mission 
from cloudmiddleware.class_link import CloudfsLinkPut

def cloudfs_link_put(request_path,dstName):
    
    path = unquote(request_path)
    newPath = '/'.join(path.split('/')[3:])
    objPath = unquote(request_path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    msgparam = {'objPath':objPath,'dstName':dstName}
    
    t = CloudfsLinkPut(newPath,msgparam)
    t = mission.execute(t)
    return t.response

