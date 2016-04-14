# -*- coding: utf-8 -*-

import json
from cloudmiddleware.task import Task

from cloudlib.urls.cloudfs import strCloudfsDirDelete,strCloudfsDirReset,strCloudfsDirDeleteRecycle,\
    strCloudfsDirMoveRecycle,strCloudfsDirPut,strCloudfsDirMove,strCloudfsDirCopy,\
    strCloudfsDirMetaGet,strCloudfsDirGet
    
class CloudfsDirDelete(Task):
    
    def __init__(self,newPath,msgparam):
        self.path = newPath
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'newPath':self.path,
                           'objPath':self.objPath})
    
    def getUrl(self):
        return strCloudfsDirDelete

class CloudfsDirPut(Task):
    
    def __init__(self,newPath,msgparam):
        self.path = newPath
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'newPath':self.path,
                           'objPath':self.objPath})
    
    def getUrl(self):
        return strCloudfsDirPut

class CloudfsDirReset(Task):
    
    def __init__(self,newPath,msgparam):
        self.path = newPath
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'newPath':self.path,
                           'objPath':self.objPath})
    
    def getUrl(self):
        return strCloudfsDirReset
    
class CloudfsDirDeleteRecycle(Task):
    
    def __init__(self,srcNewPath,dstNewPath,msgparam):
        self.srcNewPath = srcNewPath
        self.dstNewPath = dstNewPath
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'srcNewPath':self.srcNewPath,
                           'dstNewPath':self.dstNewPath,
                           'objPath':self.objPath})
    
    def getUrl(self):
        return strCloudfsDirDeleteRecycle
    
class CloudfsDirMoveRecycle(Task):
    
    def __init__(self,srcNewPath,dstNewPath,msgparam):
        self.srcNewPath = srcNewPath
        self.dstNewPath = dstNewPath
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'srcNewPath':self.srcNewPath,
                           'dstNewPath':self.dstNewPath,
                           'objPath':self.objPath})
    
    def getUrl(self):
        return strCloudfsDirMoveRecycle
    
class CloudfsDirMove(Task):
    
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
        return strCloudfsDirMove
    
class CloudfsDirCopy(Task):
    
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
        return strCloudfsDirCopy
    
class CloudfsDirMetaGet(Task):
    def __init__(self,msgparam):
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'objPath':self.objPath})
    
    def getUrl(self):
        return strCloudfsDirMetaGet
    
class CloudfsDirGet(Task):
    def __init__(self,msgparam):
        self.objPath = msgparam.get('objPath')
        
    def getBody(self):
        return json.dumps({'objPath':self.objPath})
    
    def getUrl(self):
        return strCloudfsDirGet
    