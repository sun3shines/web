# -*- coding: utf-8 -*-

import threading

class CacheUser:
    
    def __init__(self):
        
        self.userinfo = {}
        self.usertoken = {}
        self.lock = threading.Lock()
        
        self.email = 'email'
        self.passwd = 'passwd'
        
    def put(self,atName,email,passwd,token):
        if self.lock.acquire():
            self.userinfo.update({atName:{self.email:email,self.passwd:passwd}})
            self.usertoken.update({atName:token})
            self.lock.release()
            
    def get_user_token(self,atName):
        return self.usertoken.get(atName)
    
    def get_user_info(self,atName):
        return self.userinfo.get(atName)
    
    def eliminate(self,atName):
        
        if self.lock.acquire():
            self.userinfo.pop(atName)
            self.usertoken.pop(atName)
            self.lock.release()
            
    


    
