# -*- coding: utf-8 -*-

import threading
from cloudmonitor.global_cache import storageQueue
from cloudmonitor.dynamic.stat_storage import get_psutil_storage

class pStatStorage(threading.Thread):
    def __init__(self,hostUuid):
        threading.Thread.__init__(self)
        self.queue = storageQueue
        self.hostUuid = hostUuid
        
    def run(self):
        for data in get_psutil_storage(self.hostUuid):
            print data

            self.queue.put(data,block=True)
    
