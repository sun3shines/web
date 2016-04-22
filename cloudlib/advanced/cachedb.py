# -*- coding: utf-8 -*-

import threading

class CacheDb:
    def __init__(self,func,lockfunc=None):
        self.d = {}
        self.func = func
        self.lockfunc = lockfunc
        self.lock = threading.Lock()
        
    def get(self,atName):
        if atName not in self.d:
            if self.lock.acquire():
                self.d.update({atName:self.func()})
                self.lock.release()
        conn = self.d.get(atName)
        if self.lockfunc:
            if conn.timeout:
                with self.lockfunc() as mylock:
                    conn.close()
                    conn.connect()
        return conn
    
    def pop(self,atName):
        if atName in self.d:
            self.d.pop(atName)
            