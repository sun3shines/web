# -*- coding: utf-8 -*-

import psutil
import datetime
import time
from cloudmonitor.globalx import PSUTIL_SERVICE_INTERVAL,SERVICE_CMDLINE
from cloudmonitor.global_cache import MONITOR_SERVICE_PROCESS

def service_iter():
    
    while True:
        for service_name,pc in SERVICE_CMDLINE.items():
            service_init_data = {'name':service_name,
                                'cmdline':' '.join(list(pc)),
                                 'active_status':'0/0',
                                 'open_files':'0',
                                 'net_connections':'0',
                                 'thread_num':'0',
                                 'cpu_utilization':'0.0',
                                 'mem_utilization':'0.0',
                                 'available':'disable',
                                 'timestamp':str(datetime.datetime.now())}
            
            psutil_pids = MONITOR_SERVICE_PROCESS.get(service_name)
            if not psutil_pids:
                # 未初始化时为None
                psutil_pids = []
                     
            cmdline = ''
            total = len(psutil_pids)
            actives = 0
            open_files = net_connections = thread_num = 0
            cpu_utilization = mem_utilization = 0.0
            
            for pid in psutil_pids:
                try:
                    p = psutil.Process(pid)
                    service_init_data.update({'available':'enable'})
                    cmdline = ' '.join(p.cmdline) 
                    if p.status not in [psutil.STATUS_ZOMBIE,psutil.STATUS_DEAD]:
                        actives = actives + 1
                    open_files = open_files + len(p.get_open_files())
                    net_connections = net_connections + len(p.get_connections())
                    thread_num = thread_num + p.get_num_threads()
                    cpu_utilization = cpu_utilization + p.get_cpu_percent()
                    mem_utilization = mem_utilization + p.get_memory_percent()
                
                except:
                    continue
            service_init_data.update({'cmdline':cmdline,
                                      'active_status':'/'.join([str(actives),str(total)]),
                                      'open_files':str(open_files),
                                      'net_connections':str(net_connections),
                                      'thread_num':str(thread_num),
                                      'cpu_utilization':str(cpu_utilization),
                                      'mem_utilization':str(mem_utilization)})
            yield service_init_data
        time.sleep(PSUTIL_SERVICE_INTERVAL)
        
        
def get_psutil_service(hostUuid):
    
    for service_init_data in service_iter():
        yield {'hostUuid':hostUuid,
               'class':'statService',
               'attr':service_init_data}
        
        
        
