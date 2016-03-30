# -*- coding: utf-8 -*-

import json

from cloudlib.missions.tasks.task import Task 
from cloudweb.core.urls import strGetServiceStatus,strGetWorkloadStatus,strGetAbnormalEvents

class ServiceStatus(Task):
    
    def __init__(self,atName):
        self.atName = atName
        
    def getUrl(self):
        return strGetServiceStatus
        
    def getBody(self):
        return json.dumps({'atName':self.atName})
    
class WorkloadStatus(Task):
    
    def __init__(self,atName):
        self.atName = atName
        
    def getUrl(self):
        return strGetWorkloadStatus
    
    def getBody(self):
        return json.dumps({'atName':self.atName})
    
class AbnormalEvents(Task):
    
    def __init__(self,atName):
        self.atName = atName
        
    def getUrl(self):
        return strGetAbnormalEvents
    
    def getBody(self):
        return json.dumps({'atName':self.atName})
    