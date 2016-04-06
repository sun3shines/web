# -*- coding: utf-8 -*-

import json
from cloudlib.missions.tasks.task import Task 
from cloudcommon.urls.web import strUserLogin,strUserList, strUserEnable,strUserDisable,strUserDelete

class UserLogin(Task):
    
    def __init__(self,email,passwd):
        
        self.email = email
        self.passwd = passwd
        
    def getUrl(self):
        return strUserLogin
    
    def getBody(self):
        
        params = {'email':self.email,
                  'passwd':self.passwd}
        
        return json.dumps(params)
    
class UserList(Task):
    
    def __init__(self,atName):
        self.atName = atName
        
    def getUrl(self):
        return strUserList
    
    def getBody(self):
        return json.dumps({'atName':self.atName})
    
class UserEnable(Task):
    
    def __init__(self,atName,urName):
        self.atName = atName
        self.urName = urName
        
    def getUrl(self):
        return strUserEnable
    
    def getBody(self):
        return json.dumps({'atName':self.atName,
                'urName':self.urName})
    
    
class UserDisable(Task):
    
    def __init__(self,atName,urName):
        self.atName = atName
        self.urName = urName
        
    def getUrl(self):
        return strUserDisable
    
    def getBody(self):
        return json.dumps({'atName':self.atName,
                'urName':self.urName})
        
class UserDelete(Task):
    
    def __init__(self,atName,urName):
        self.atName = atName
        self.urName = urName
        
    def getUrl(self):
        return strUserDelete
    
    def getBody(self):
        return json.dumps({'atName':self.atName,
                'urName':self.urName})
        
