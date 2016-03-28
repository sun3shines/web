# -*- coding: utf-8 -*-

import json
from cloudweb.missions.tasks.task import Task 
from cloudweb.core.urls import strGetAtRecords,strGetOtRecords

class ObjectRecord(Task):
    def __init__(self,atName,objPath):
        self.atName = atName
        self.objPath = objPath
        
    def getUrl(self):
        return strGetOtRecords
    
    def getBody(self):
        return json.dumps({'atName':self.atName,
                'objPath':self.objPath})
        
        
class AccountRecord(Task):
    def __init__(self,atName):
        self.atName = atName
        
    def getUrl(self):
        return strGetAtRecords
    
    def getBody(self):
        return json.dumps({'atName':self.atName})
    
    
