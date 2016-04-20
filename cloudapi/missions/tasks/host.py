# -*- coding: utf-8 -*-

import json

from cloudapi.missions.tasks.task import Task 
from cloudlib.urls.flask import strGetServiceStatus,strGetWorkloadStatus,strGetAbnormalEvents,\
    strGetHostStatic

class HostStatic(Task):
    
    def __init__(self,atName):
        self.atName = atName
        
    def getUrl(self):
        return strGetHostStatic
    
    def getBody(self):
        return json.dumps({'atName':self.atName})
        
class ServiceStatus(Task):
    
    def __init__(self,atName,hostUuid):
        self.atName = atName
        self.hostUuid = hostUuid
        
    def getUrl(self):
        return strGetServiceStatus
        
    def getBody(self):
        return json.dumps({'atName':self.atName,
                           'hostUuid':self.hostUuid})
    
class WorkloadStatus(Task):
    
    def __init__(self,atName,hostUuid,className):
        self.atName = atName
        self.hostUuid = hostUuid
        self.className = className
        
    def getUrl(self):
        return strGetWorkloadStatus
    
    def getBody(self):
        return json.dumps({'atName':self.atName,
                           'hostUuid':self.hostUuid,
                           'className':self.className})
    
class AbnormalEvents(Task):
    
    def __init__(self,atName):
        self.atName = atName
        
    def getUrl(self):
        return strGetAbnormalEvents
    
    def getBody(self):
        return json.dumps({'atName':self.atName})
    