# -*- coding: utf-8 -*-

import json
from cloudmiddleware.task import Task
from cloudlib.urls.cloudfs import strCloudfsOauthRegister,strCloudfsTokenValid

class OauthRegister(Task):
    
    def __init__(self,email,passwd,usertoken):
        self.email = email
        self.passwd = passwd
        self.usertoken = usertoken
        
    def getBody(self):
        return json.dumps({'email':self.email,
                           'passwd':self.passwd,
                           'usertoken':self.usertoken})
    
    def getUrl(self):
        return strCloudfsOauthRegister
    
class OauthTokenValid(Task):
    
    def __init__(self,usertoken):
        self.usertoken = usertoken
        
    def getBody(self):
        return json.dumps({'usertoken':self.usertoken})
    
    def getUrl(self):
        return strCloudfsTokenValid
    