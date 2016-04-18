# -*- coding: utf-8 -*-

import threading

class CacheConsistency:
    def __init__(self):
        self.d = {}
        self.lock = threading.Lock()
        
        self.success = 'successed'
        self.running = 'running'
    
    def get(self,atName):
        if atName not in self.d:
            return None
        return self.d.get(atName)
    
    def pop(self,atName):
        if atName in self.d:
            self.d.pop(atName)
    
    def put(self,atName,status):
        if self.lock.acquire():
            self.d.update({atName:status})
            self.lock.release()
            
    def successed(self,atName):
        return self.success == self.get(atName)
    
    def waiting(self,atName):
        return self.running == self.get(atName)
    
    def failed(self,atName):
        return not self.get(atName)
    
    def eliminate(self,atName):
        
        if self.lock.acquire():
            self.pop(atName)
            self.lock.release()
            
        