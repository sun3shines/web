# -*- coding: utf-8 -*-

import threading
from cloudmonitor.global_cache import memQueue
from cloudmonitor.dynamic.stat_mem import get_psutil_memory

class pStatMem(threading.Thread):
    def __init__(self,hostUuid):
        threading.Thread.__init__(self)
        self.queue = memQueue
        self.hostUuid = hostUuid
        
    def run(self):
        for data in get_psutil_memory(self.hostUuid):
            print data

            self.queue.put(data,block=True)
    
