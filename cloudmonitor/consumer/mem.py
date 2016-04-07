# -*- coding: utf-8 -*-

import threading
from cloudmonitor.global_cache import memQueue
from cloudmonitor.http.api import monitor_stat

class cStatMem(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.queue = memQueue
        
    def run(self):
        while True:
            monitor_stat(self.queue.get())
    
    