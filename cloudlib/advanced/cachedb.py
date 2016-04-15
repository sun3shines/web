# -*- coding: utf-8 -*-

class CacheDb:
    def __init__(self,func):
        self.d = {}
        self.func = func
        
    def get(self,atName):
        if atName not in self.d:
            self.d.update({atName:self.func()})
        return self.d.get(atName)
    
    def pop(self,atName):
        if atName in self.d:
            self.d.pop(atName)
            