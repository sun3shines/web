# -*- coding: utf-8 -*-

import threading
class CacheDb:
    def __init__(self,func):
        self.d = {}
        self.func = func
        self.lock = threading.Lock()
        
    def get(self,atName):
        if atName not in self.d:
            if self.lock.acquire():
                self.d.update({atName:self.func()})
                self.lock.release()
        return self.d.get(atName)
    
    def pop(self,atName):
        if atName in self.d:
            self.d.pop(atName)
            