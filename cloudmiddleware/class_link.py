# -*- coding: utf-8 -*-

import json
from cloudmiddleware.task import Task
from cloudlib.urls.cloudfs import strCloudfsLinkPut

class CloudfsLinkPut(Task):
    
    def __init__(self,newPath,msgparam):
        self.newPath = newPath
        self.objPath = msgparam.get('objPath')
        self.dstName = msgparam.get('dstName')
        
    def getBody(self):
        return json.dumps({'newPath':self.newPath,
                           'objPath':self.objPath,
                           'dstName':self.dstName})
    
    def getUrl(self):
        return strCloudfsLinkPut