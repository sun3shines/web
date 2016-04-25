# -*- coding: utf-8 -*-

import json

from cloudapi.missions.tasks.task import Task 
from cloudlib.urls.flask import strExecutorAdd,strExecutorDel,strExecutorList,\
    strConfigGet,strConfigSet

class ExecutorAdd(Task):
    
    def __init__(self,atName,hostip):
        self.atName = atName
        self.hostip = hostip
        
    def getUrl(self):
        return strExecutorAdd
    
    def getBody(self):
        return json.dumps({'atName':self.atName,
                           'hostip':self.hostip})
        
class ExecutorDel(Task):
    def __init__(self,atName,hostUuid):
        self.atName = atName
        self.hostUuid = hostUuid
        
    def getUrl(self):
        return strExecutorDel
    
    def getBody(self):
        return json.dumps({'atName':self.atName,
                           'hostUuid':self.hostUuid})
        
class ExecutorList(Task):
    def __init__(self,atName):
        self.atName = atName
        
    def getUrl(self):
        return strExecutorList
    
    def getBody(self):
        return json.dumps({'atName':self.atName})      
              
class ConfigGet(Task):
    def __init__(self,atName,hostUuid):
        self.atName = atName
        self.hostUuid = hostUuid
        
    def getUrl(self):
        return strConfigGet
    
    def getBody(self):
        return json.dumps({'atName':self.atName,
                           'hostUuid':self.hostUuid})
        
class ConfigSet(Task):
    def __init__(self,atName,hostUuid,attrs):
        self.atName = atName
        self.hostUuid = hostUuid
        self.attrs = attrs
        
    def getUrl(self):
        return strConfigSet
    
    def getBody(self):
        return json.dumps({'atName':self.atName,
                           'hostUuid':self.hostUuid,
                           'confAttrs':self.attrs})
     