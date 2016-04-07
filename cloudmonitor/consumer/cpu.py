# -*- coding: utf-8 -*-

import threading
from cloudmonitor.global_cache import cpuQueue
from cloudmonitor.http.api import monitor_stat
class cStatCpu(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.queue = cpuQueue
        
    def run(self):
        while True:
#            data = self.queue.get()
#            print data
            monitor_stat(self.queue.get())
    
