
import json
from cloudmiddleware.task import Task
from cloudlib.urls.cloudfs import strCloudfsAccountValid,strCloudfsObjectValid

class CloudfsAccountValid(Task):
    def __init__(self,newPath):
        self.path = newPath
        
    def getBody(self):
        return json.dumps({'newPath':self.path})
    
    def getUrl(self):
        return strCloudfsAccountValid
    
class CloudfsObjectValid(Task):
    
    def __init__(self,newPath):
        self.path = newPath
        
    def getBody(self):
        return json.dumps({'newPath':self.path})
    
    def getUrl(self):
        return strCloudfsObjectValid