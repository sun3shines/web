# -*- coding: utf-8 -*-

import threading

class CacheConsistency:
    def __init__(self):
        self.d = {}
        self.lock = threading.Lock()
        
        self.state_success = 'success'
        self.state_running = 'running'
    
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
            
    def success(self,atName):
        return self.state_success == self.get(atName)
    
    def running(self,atName):
        return self.state_running == self.get(atName)
    
    def failed(self,atName):
        return not self.get(atName)
    
    def eliminate(self,atName):
        
        if self.lock.acquire():
            self.pop(atName)
            self.lock.release()
            
        