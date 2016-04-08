# -*- coding: utf-8 -*-

import psutil
import threading
import time
from cloudmonitor.globalx import PSUTIL_PROCESS_INTERVAL
from cloudmonitor.global_cache import MONITOR_DISK_PROCESS
from cloudmonitor.globalx import CLOUD_CMDLINES

def is_cloud_process(cmdline):
    
    for c in CLOUD_CMDLINES:
        i = 0
        while i< len(c):
            if c[i] != cmdline[i]:
                break
        if len(c) == i:
            return True
    return False
            
def get_psutil_process():
    
    while True:
        pids = []
        for p in psutil.process_iter():
            if is_cloud_process(p.cmdline):
                pids.append(p.pid)
        yield pids
        time.sleep(PSUTIL_PROCESS_INTERVAL)
        
class ProcessFilter(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        for pids in get_psutil_process():
            print 'monitor process: ',pids
            MONITOR_DISK_PROCESS.set(pids)
            
    
