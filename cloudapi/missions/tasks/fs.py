# -*- coding: utf-8 -*-

import json
from cloudapi.missions.tasks.task import Task 
from cloudlib.urls.flask import strAccountList, strContainerList, strDirList
class AccountList(Task):
    
    def __init__(self,atName):
        self.atName = atName
        
    def getBody(self):
        return json.dumps({'atName':self.atName})
    
    def getUrl(self):
        return strAccountList
    
    
class ContainerList(Task):
    def __init__(self,atName,cntPath,tree=False):
        self.atName = atName
        self.cntPath = cntPath
        self.tree = tree
        
    def getBody(self):
        return json.dumps({'atName':self.atName,
                           'cntPath':self.cntPath,
                           'tree':str(self.tree).lower()})
        
    def getUrl(self):
        return strContainerList
    
class DirList(Task):
    def __init__(self,atName,drPath,tree=False):
        self.atName = atName
        self.drPath = drPath
        self.tree = tree
        
    def getBody(self):
        return json.dumps({'atName':self.atName,
                           'drPath':self.drPath,
                           'tree':str(self.tree).lower()})
        
    def getUrl(self):
        return strDirList
    
