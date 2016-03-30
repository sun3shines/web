# -*- coding: utf-8 -*-

import json

from cloudlib.missions.tasks.task import Task 
from cloudweb.core.urls import strObjectDetails,strDisableObject,strEnableObject,strDeleteObject, \
    strDownloadObject,strUploadObject

#class ObjectDetails(Task):
    
#    def __init__(self,atName,objectId):
#        self.atName = atName
#        self.objectId = objectId
        
#    def getUrl(self):
#        return strObjectDetails
    
#    def getBody(self):
#        return json.dumps({'atName':self.atName,
#                           'objectId':self.objectId})
        

    
class ObjectDisable(Task):
    
    def __init__(self,atName,objPath):
        
        self.atName = atName
        self.objPath = objPath
        
    def getUrl(self):
        return strDisableObject
    
    def getBody(self):
        return json.dumps({'atName':self.atName,
                           'objPath':self.objPath})
        
class ObjectEnable(Task):
    
    def __init__(self,atName,objPath):
        
        self.atName = atName
        self.objPath = objPath
        
    def getUrl(self):
        
        return strEnableObject
    
    def getBody(self):
        return json.dumps({'atName':self.atName,
                           'objPath':self.objPath})
        
class ObjectDelete(Task):
    
    def __init__(self,atName,objPath):
        
        self.atName = atName
        self.objPath = objPath
        
    def getUrl(self):
        return strDeleteObject
    
    def getBody(self):
        return json.dumps({'atName':self.atName,
                           'objPath':self.objPath})
        
class ObjectDownload(Task):
    
    def __init__(self,atName,objPath):
        
        self.atName = atName
        self.objPath = objPath
        
    def getUrl(self):
        return strDownloadObject
    
    def getBody(self):
        return json.dumps({'atName':self.atName,
                           'objPath':self.objPath})

class ObjectUpload(Task):

    def __init__(self,atName,obj,localPath):
        self.atName = atName
        self.obj = obj 
        self.localPath = localPath

    def getUrl(self):
        return strUploadObject

    def getHeaders(self):
        return {'atName':self.atName,
                'objPath':self.obj}

    def getBody(self):
        return file(self.localPath)

