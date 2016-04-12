# -*- coding: utf-8 -*-

import json
from cloudapi.missions.tasks.task import Task
from cloudlib.urls.flask import strDataGlobalSearch,strDataMd5Search,strDataUserSearch,strObjectDetails

class UserSearch(Task):
    
    def __init__(self,atName,keyWord):
        self.atName = atName
        self.keyWord = keyWord
        
    def getUrl(self):
        
        return strDataUserSearch
    
    def getBody(self):
        
        params = {'atName':self.atName,
                  'keyword':self.keyWord}
        return json.dumps(params)
    
class GlobalSearch(Task):
    
    def __init__(self,atName,keyWord):
        self.keyWord = keyWord
        self.atName = atName # must be admin type
        
    def getUrl(self):
        return strDataGlobalSearch
    
    def getBody(self):
        
        return json.dumps({'atName':self.atName,
                           'keyword':self.keyWord})
    
class Md5Search(Task):
    
    def __init__(self,md5):
        self.md5 = md5
        
    def getUrl(self):
        return strDataMd5Search
    
    def getBody(self):
        
        return json.dumps({'md5':self.md5}) 

class ObjectDetails(Task):

    def __init__(self,atName,objectId):
        self.atName = atName
        self.objectId = objectId

    def getUrl(self):
        return strObjectDetails

    def getBody(self):
        return json.dumps({'atName':self.atName,
                           'objectId':self.objectId})

