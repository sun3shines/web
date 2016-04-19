# -*- coding: utf-8 -*-

import Queue
import threading
import time
class CacheQueue:
    def __init__(self):
        self.d = {}
        self.lock = threading.Lock()
        
    def get(self,atName):
        if atName not in self.d:
            if self.lock.acquire():
                self.d.update({atName:Queue.Queue()})
                self.lock.release()
        return self.d.get(atName)
    
    def pop(self,atName):
        if atName in self.d:
            self.d.pop(atName)
            
    def put_consistency(self,atName):
        
        q = self.get(atName)
        if q.empty():
            q.put(time.time())
            
    def get_consistency(self,atName):
        q = self.get(atName)
        if not q.empty():
            return q.get()
        return None
    