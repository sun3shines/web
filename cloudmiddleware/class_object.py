# -*- coding: utf-8 -*-

import json
from cloudmiddleware.task import Task
from cloudlib.urls.cloudfs import strCloudfsObjectPut,strCloudfsObjectDelete,strCloudfsObjectDeleteRecycle,\
    strCloudfsObjectCopy,strCloudfsObjectMove,strCloudfsObjectMoveRecycle,strCloudfsObjectGet,strCloudfsObjectHead,\
    strCloudfsObjectMeta,strCloudfsObjectPost
    
class CloudfsObjectPut(Task):
    def __init__(self,newPath,msgparam):
        self.path = newPath
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'newPath':self.path,
                           'objPath':self.objPath})
    
    def getUrl(self):
        return strCloudfsObjectPut
    
class CloudfsObjectDelete(Task):
    def __init__(self,newPath,msgparam):
        self.path = newPath
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'newPath':self.path,
                           'objPath':self.objPath})
    
    def getUrl(self):
        return strCloudfsObjectDelete
    
class CloudfsObjectDeleteRecycle(Task):
    def __init__(self,srcNewPath,dstNewPath,msgparam):
        self.srcNewPath = srcNewPath
        self.dstNewPath = dstNewPath
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'srcNewPath':self.srcNewPath,
                           'dstNewPath':self.dstNewPath,
                           'objPath':self.objPath})
    
    def getUrl(self):
        return strCloudfsObjectDeleteRecycle
    
class CloudfsObjectCopy(Task):
    def __init__(self,srcNewPath,dstNewPath,msgparam):
        self.srcNewPath = srcNewPath
        self.dstNewPath = dstNewPath
        self.objPath = msgparam.get('objPath')
        self.dstName = msgparam.get('dstName')
        
    def getBody(self):
        return json.dumps({'srcNewPath':self.srcNewPath,
                           'dstNewPath':self.dstNewPath,
                           'objPath':self.objPath,
                           'dstName':self.dstName})
    
    def getUrl(self):
        return strCloudfsObjectCopy

class CloudfsObjectMove(Task):
    def __init__(self,srcNewPath,dstNewPath,msgparam):
        self.srcNewPath = srcNewPath
        self.dstNewPath = dstNewPath
        self.objPath = msgparam.get('objPath')
        self.dstName = msgparam.get('dstName')
                
    def getBody(self):
        return json.dumps({'srcNewPath':self.srcNewPath,
                           'dstNewPath':self.dstNewPath,
                           'objPath':self.objPath,
                           'dstName':self.dstName})
    
    def getUrl(self):
        return strCloudfsObjectMove
    
    
class CloudfsObjectMoveRecycle(Task):
    def __init__(self,srcNewPath,dstNewPath,msgparam):
        self.srcNewPath = srcNewPath
        self.dstNewPath = dstNewPath
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'srcNewPath':self.srcNewPath,
                           'dstNewPath':self.dstNewPath,
                           'objPath':self.objPath})
    
    def getUrl(self):
        return strCloudfsObjectMoveRecycle  
    
class CloudfsObjectGet(Task):
    def __init__(self,msgparam):
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'objPath':self.objPath})
    
    def getUrl(self):
        return strCloudfsObjectGet

class CloudfsObjectHead(Task):
    def __init__(self,msgparam):
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'objPath':self.objPath})
    
    def getUrl(self):
        return strCloudfsObjectHead
    
class CloudfsObjectMeta(Task):
    def __init__(self,msgparam):
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'objPath':self.objPath})
    
    def getUrl(self):
        return strCloudfsObjectMeta

class CloudfsObjectPost(Task):
    def __init__(self,msgparam):
        self.objPath = msgparam.get('objPath')
        self.header = msgparam.get('header')
        
    def getBody(self):
        return json.dumps({'objPath':self.objPath,
                           'header':self.header})
    
    def getUrl(self):
        return strCloudfsObjectPost
    
    