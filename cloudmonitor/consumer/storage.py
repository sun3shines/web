# -*- coding: utf-8 -*-

import threading
from cloudmonitor.global_cache import storageQueue
from cloudmonitor.http.api import monitor_stat

class cStatStorage(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.queue = storageQueue
        
    def run(self):
        while True:
            monitor_stat(self.queue.get())
    
    
    