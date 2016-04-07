# -*- coding: utf-8 -*-

import psutil
import datetime

from cloudmonitor.globalx import PSUTIL_CPU_INTERVAL

def cpu_iter():
    
    while True:
        yield psutil.cpu_percent(PSUTIL_CPU_INTERVAL)
        
def get_psutil_cpu(hostUuid):
    
    for utilization in cpu_iter():
        yield {'hostUuid':hostUuid,
                'class':'statCpu',
                'attr':{'utilization':utilization,
                'timestamp':str(datetime.datetime.now())}}
        
        
        