# -*- coding: utf-8 -*-

import threading

class lockList:
    
    def __init__(self):
        
        self.l = []
        self.lock = threading.Lock()
        
    def set(self,l):
        if self.lock.acquire():
            self.l = l
            self.lock.release()
            
    def get(self):
        return self.l
    
    def delete(self,pid):
        if self.lock.acquire():
            self.l.remove(pid)
            self.lock.release()       


    
