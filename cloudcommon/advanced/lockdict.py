# -*- coding: utf-8 -*-

import threading

class lockDict:
    
    def __init__(self):
        
        self.d = {}
        self.lock = threading.Lock()
        
    def put(self,key,val):
        if self.lock.acquire():
            self.d.update({key:val})
            self.lock.release()
            
    def get(self,key):
        return self.d.get(key)
    


    
