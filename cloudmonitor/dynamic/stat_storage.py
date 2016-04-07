# -*- coding: utf-8 -*-
import psutil
import time
import datetime

from cloudmonitor.globalx import PSUTIL_STORAGE_INTERVAL,MONITOR_ALLOWD_FSTYPE
from cloudmonitor.md5 import str2uuid

def storage_iter():
    
    while True:
        time.sleep(PSUTIL_STORAGE_INTERVAL)
        for p in psutil.disk_partitions():
            if p.fstype not in MONITOR_ALLOWD_FSTYPE:
                continue
            u = psutil.disk_usage(p.mountpoint)
            path = p.mountpoint
            uuid = str2uuid(p.mountpoint)
            yield uuid,path,u.total,u.used,u.free
        
def get_psutil_storage(hostUuid):
    
    for uuid,path,total,used,free in storage_iter():
        yield {'hostUuid':hostUuid,
               'class':'statStorage',
               'attr':{'timestamp':str(datetime.datetime.now()),
                       'uuid':uuid,
                       'path':path,
                       'total':total,
                       'used':used,
                       'free':free,
                       'available':'enable'}}
        