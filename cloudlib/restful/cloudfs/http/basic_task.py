# -*- coding: utf-8 -*-

import urllib
import json

from cloudlib.restful.cloudfs.http.task import Task

class UfoContainerList(Task):
    pass

class UfoContainerCreate(Task):
    def __init__(self,cnt):
        self.cnt = urllib.quote(cnt)
    def getMethod(self):
        return 'PUT'
    def getPartialUrl(self):
        return self.cnt
    
class UfoContainerDelete(Task):
    def __init__(self,cnt):
        self.cnt = urllib.quote(cnt)
        
    def getMethod(self):
        return 'DELETE'
    
    def getPartialUrl(self):
        return self.cnt
    
class UfoObjectList(Task):
    
    def __init__(self,cnt,r=False):
        self.cnt = urllib.quote(cnt)
        self.r = r
    def getParams(self):
        return {'op':'LISTDIR',
                'recursive':str(self.r).lower()}
        
    def getPartialUrl(self):
        return self.cnt
    
class UfoObjectCreate(Task):
    
    def __init__(self,obj,srcPath='',handle=None):
        self.obj = urllib.quote(obj)
        self.srcPath = urllib.quote(srcPath)
        self.handle = handle
    def getMethod(self):
        return 'PUT'
    
    def getPartialUrl(self):
        return self.obj
    
    def getBody(self):
        if self.srcPath:
            return open(self.srcPath)
        else:
            return self.handle

    
class UfoObjectDelete(Task):
    
    def __init__(self,obj):
        self.obj = urllib.quote(obj)
        
    def getPartialUrl(self):
        return self.obj
    
    def getMethod(self):
        return 'DELETE'
    
class UfoObjectCopy(Task):
    
    def __init__(self,obj ,dst):
        self.obj = urllib.quote(obj)
        self.dst = urllib.quote(dst)
        
    def getMethod(self):
        return 'COPY'
    
    def getPartialUrl(self):
        return self.obj
    def getHeaders(self):
        return {'Destination':self.dst}
    
class UfoObjectGet(Task):
    
    def __init__(self,obj):
        self.obj = urllib.quote(obj)
        
    def getPartialUrl(self):
        return self.obj

class UfoAccountMeta(Task):
    
    def getMethod(self):
        return 'META'
    
class UfoContainerMeta(Task):
    def __init__(self,cnt):
        
        self.cnt = urllib.quote(cnt)
        
    def getPartialUrl(self):
        return self.cnt
    
    def getMethod(self):
        return 'META'
