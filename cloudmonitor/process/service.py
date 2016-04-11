# -*- coding: utf-8 -*-

import psutil
import threading
import time
from cloudmonitor.globalx import PSUTIL_SERVICE_INTERVAL
from cloudmonitor.global_cache import MONITOR_SERVICE_PROCESS
from cloudmonitor.globalx import SERVICE_CMDLINE

def is_cloud_service(cmdline):
    for service_name,pc in SERVICE_CMDLINE.items():
        if len(cmdline) < len(pc):
            return ''
        i = 0
        while i< len(pc):
            if pc[i] != cmdline[i]:
                break
            i = i + 1
        if len(pc) == i:
            return service_name
    return ''
            
def get_psutil_service():

    while True:
        srvpids = {}
        for service_name in SERVICE_CMDLINE:
            srvpids.update({service_name:[]})
        
        for p in psutil.process_iter():
            service_name = is_cloud_service(p.cmdline)
            if service_name:
                srvpids.get(service_name).append(p.pid)
        yield srvpids
        time.sleep(PSUTIL_SERVICE_INTERVAL)
        
class ServiceFilter(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        for srvpids in get_psutil_service():
            print 'monitor service: ',srvpids
            for key,vals in srvpids.items():
                MONITOR_SERVICE_PROCESS.put(key, vals)
                
