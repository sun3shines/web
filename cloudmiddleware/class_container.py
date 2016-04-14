# -*- coding: utf-8 -*-

import json
from cloudmiddleware.task import Task
from cloudlib.urls.cloudfs import strCloudfsContainerDelete,strCloudfsContainerPut,strCloudfsContainerHead,\
    strCloudfsContainerMeta,strCloudfsContainerGet,strCloudfsContainerPost

class CloudfsContainerDelete(Task):
    def __init__(self,newpath,msgparam):
        self.path = newpath
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'newPath':self.path,
                           'objPath':self.objPath})

    def getUrl(self):
        return strCloudfsContainerDelete
    
class CloudfsContainerPut(Task):
    def __init__(self,newpath,msgparam):
        self.path = newpath
        self.objPath = msgparam.get('objPath')
    def getBody(self):
        return json.dumps({'newPath':self.path,
                           'objPath':self.objPath})

    def getUrl(self):
        return strCloudfsContainerPut
    
class CloudfsContainerHead(Task):
    def __init__(self,msgparam):
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'objPath':self.objPath})

    def getUrl(self):
        return strCloudfsContainerHead
    
class CloudfsContainerMeta(Task):
    def __init__(self,msgparam):
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'objPath':self.objPath})

    def getUrl(self):
        return strCloudfsContainerMeta
    
class CloudfsContainerGet(Task):
    def __init__(self,msgparam):
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'objPath':self.objPath})

    def getUrl(self):
        return strCloudfsContainerGet
 
class CloudfsContainerPost(Task):
    def __init__(self,msgparam):
        self.objPath = msgparam.get('objPath')
        self.header = msgparam.get('header')
        
    def getBody(self):
        return json.dumps({'objPath':self.objPath,
                           'header':self.header})

    def getUrl(self):
        return strCloudfsContainerPost   
    