# -*- coding: utf-8 -*-

import threading
from cloudmonitor.global_cache import serviceQueue
from cloudmonitor.dynamic.stat_service import get_psutil_service

class pStatService(threading.Thread):
    def __init__(self,hostUuid):
        threading.Thread.__init__(self)
        self.queue = serviceQueue
        self.hostUuid = hostUuid
        
    def run(self):
        for data in get_psutil_service(self.hostUuid):
            print data
            self.queue.put(data,block=True)
    
