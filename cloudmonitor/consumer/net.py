# -*- coding: utf-8 -*-

import threading
from cloudmonitor.global_cache import netQueue
from cloudmonitor.http.api import monitor_stat

class cStatNet(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.queue = netQueue
        
    def run(self):
        while True:
            monitor_stat(self.queue.get())
    
    