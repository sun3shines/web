# -*- coding: utf-8 -*-

import json
from cloudweb.missions.tasks.task import Task 
from cloudweb.core.urls import strAccountList, strContainerList, strDirList
class AccountList(Task):
    
    def __init__(self,atName):
        self.atName = atName
        
    def getBody(self):
        return json.dumps({'atName':self.atName})
    
    def getUrl(self):
        return strAccountList
    
    
class ContainerList(Task):
    def __init__(self,atName,cntPath):
        self.atName = atName
        self.cntPath = cntPath
        
    def getBody(self):
        return json.dumps({'atName':self.atName,
                           'cntPath':self.cntPath})
        
    def getUrl(self):
        return strContainerList
    
class DirList(Task):
    def __init__(self,atName,drPath):
        self.atName = atName
        self.drPath = drPath
        
    def getBody(self):
        return json.dumps({'atName':self.atName,
                           'drPath':self.drPath})
        
    def getUrl(self):
        return strDirList
    
