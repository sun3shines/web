# -*- coding: utf-8 -*-

import threading
from cloudmonitor.global_cache import netQueue
from cloudmonitor.dynamic.stat_net import get_psutil_net

class pStatNet(threading.Thread):
    def __init__(self,hostUuid):
        threading.Thread.__init__(self)
        self.queue = netQueue
        self.hostUuid = hostUuid
        
    def run(self):
        for data in get_psutil_net(self.hostUuid):
            print data

            self.queue.put(data,block=True)
    
