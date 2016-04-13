# -*- coding: utf-8 -*-

import json
from cloudmiddleware.task import Task
from cloudlib.urls.cloudfs import strCloudfsAccountPut,strCloudfsAccountDelete,strCloudfsAccountValid

class CloudAccountPut(Task):
    def __init__(self,path):
        self.path = path
        
    def getBody(self):
        return json.dumps({'atName':self.path})
    
    def getUrl(self):
        return strCloudfsAccountPut
    
    
class CloudAccountDelete(Task):
    def __init__(self,path):
        self.path = path
        
    def getBody(self):
        return json.dumps({'atName':self.path})
    
    def getUrl(self):
        return strCloudfsAccountDelete
    
class CloudAccountValid(Task):
    def __init__(self,request_path):
        self.path = request_path
        
    def getBody(self):
        return json.dumps({'atName':self.path})
    
    def getUrl(self):
        return strCloudfsAccountValid
    
    
    