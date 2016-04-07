# -*- coding: utf-8 -*-

import threading
from cloudmonitor.global_cache import cpuQueue
from cloudmonitor.dynamic.stat_cpu import get_psutil_cpu

class pStatCpu(threading.Thread):
    def __init__(self,hostUuid):
        threading.Thread.__init__(self)
        self.queue = cpuQueue
        self.hostUuid = hostUuid
        
    def run(self):
        for data in get_psutil_cpu(self.hostUuid):
            print data

            self.queue.put(data,block=True)
    
