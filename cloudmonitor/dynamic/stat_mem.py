# -*- coding: utf-8 -*-

import psutil
import datetime
import time
from cloudmonitor.globalx import PSUTIL_MEM_INTERVAL

def memory_iter():
    
    while True:
        time.sleep(PSUTIL_MEM_INTERVAL)
        m = psutil.virtual_memory()
        yield (m.total,m.available)
        
def get_psutil_memory(hostUuid):
    
    for total,available in memory_iter():
        yield {'hostUuid':hostUuid,
                'class':'statMem',
                'attr':{'total':total,'available':available,
                'timestamp':str(datetime.datetime.now())}}
        
        
        