# -*- coding: utf-8 -*-

class Cache:
    def __init__(self):
        
        self.data = {}
        self.lock = None
        
    def setCache(self,key,value):
        
        self.data[key] = value
        
    def getCache(self,key):
        return self.data.get(key)
    
    
class UserCache(Cache):
    
    def setUser(self,key,value):
        self.setCache(key, value)
        
    def getUser(self,key):
        return self.getCache(key)
        
    
class TokenCache(Cache):
    
    def setToken(self,key,value):
        self.setCache(key, value)
        
    def getToken(self,key):
        return self.getCache(key)
        
        