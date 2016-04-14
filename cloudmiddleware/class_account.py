# -*- coding: utf-8 -*-

import json
from cloudmiddleware.task import Task
from cloudlib.urls.cloudfs import strCloudfsAccountPut,strCloudfsAccountDelete,strCloudfsAccountValid,\
    strCloudfsAccountExists,strCloudfsAccountHead,strCloudfsAccountGet,strCloudfsAccountMeta,\
    strCloudfsAccountPost

class CloudfsAccountPut(Task):
    def __init__(self,newPath,msgparam):
        self.path = newPath
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'newPath':self.path,
                           'objPath':self.objPath})
    
    def getUrl(self):
        return strCloudfsAccountPut
    
class CloudfsAccountDelete(Task):
    def __init__(self,newPath):
        self.path = newPath
        
    def getBody(self):
        return json.dumps({'newPath':self.path})
    
    def getUrl(self):
        return strCloudfsAccountDelete
        
class CloudfsAccountExists(Task):
    def __init__(self,newPath):
        self.path = newPath
        
    def getBody(self):
        return json.dumps({'newPath':self.path})
    
    def getUrl(self):
        return strCloudfsAccountExists
    
class CloudfsAccountHead(Task):
    def __init__(self,msgparam):
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'objPath':self.objPath})
    
    def getUrl(self):
        return strCloudfsAccountHead
    
class CloudfsAccountGet(Task):
    def __init__(self,msgparam):
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'objPath':self.objPath})
    
    def getUrl(self):
        return strCloudfsAccountGet
    
class CloudfsAccountMeta(Task):
    def __init__(self,msgparam):
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'objPath':self.objPath})
    
    def getUrl(self):
        return strCloudfsAccountMeta
    
class CloudfsAccountPost(Task):
    def __init__(self,msgparam):
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'objPath':self.objPath})
    
    def getUrl(self):
        return strCloudfsAccountPost
    
    
    
    