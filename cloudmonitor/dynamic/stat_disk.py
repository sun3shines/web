# -*- coding: utf-8 -*-

import psutil
import datetime
import time
from cloudmonitor.globalx import PSUTIL_DISK_INTERVAL
from cloudmonitor.global_cache import MONITOR_DISK_PROCESS

def psutil_process_bytes(psutil_pids):
    
    read_bytes = {}
    write_bytes = {}
    delpids = []
    
    for pid in psutil_pids:
        try:
            f = psutil.Process(pid).get_io_counters()
            read_bytes.update({pid:f.read_bytes})
            write_bytes.update({pid:f.write_bytes})
        except:
            if read_bytes.has_key(pid):
                read_bytes.pop(pid)
            if write_bytes.has_key(pid):
                write_bytes.pop(pid)
            delpids.append(pid)
            
    for pid in delpids:
        psutil_pids.remove(pid)
    print read_bytes,write_bytes        
    return read_bytes,write_bytes

                                
def disk_iter():
    
    read_bytes_before = write_bytes_before = None
    read_bytes_after = write_bytes_after = None
     
    while True:
        psutil_pids = MONITOR_DISK_PROCESS.get()
        if not read_bytes_before or not write_bytes_before :
            read_bytes_before,write_bytes_before = psutil_process_bytes(psutil_pids)
        else:
            read_bytes_before,write_bytes_before = read_bytes_after,write_bytes_after
            
        time.sleep(PSUTIL_DISK_INTERVAL)
        read_bytes_after,write_bytes_after = psutil_process_bytes(psutil_pids)
        
        read_total_bytes = write_total_bytes = 0
        read_bytes_per_sec = write_bytes_per_sec = 0
        
        for pid in psutil_pids:
            read_total_bytes = read_total_bytes + read_bytes_after[pid] - read_bytes_before[pid]
            write_total_bytes = write_total_bytes + write_bytes_after[pid] - write_bytes_before[pid]
        read_bytes_per_sec = read_total_bytes/PSUTIL_DISK_INTERVAL
        write_bytes_per_sec = write_total_bytes/PSUTIL_DISK_INTERVAL
        yield read_bytes_per_sec,write_bytes_per_sec
        
        
def get_psutil_disk(hostUuid):
    
    for disk_read_per_sec,disk_write_per_sec in disk_iter():
        yield {'hostUuid':hostUuid,
               'class':'statDisk',
               'attr':{'timestamp':str(datetime.datetime.now()),
                       'disk_read_per_sec':disk_read_per_sec,
                       'disk_write_per_sec':disk_write_per_sec}}
        
        
        
