# -*- coding: utf-8 -*-

from cloudmonitor.http.api import monitor_start,monitor_stat
from cloudmonitor.static.host import get_host_static

from cloudmonitor.dynamic.stat_cpu import get_psutil_cpu

if __name__ == '__main__':

    host_hw = get_host_static()
#    import pdb;pdb.set_trace()
    monitor_start(host_hw)
    
    hostUuid = host_hw.get('hostUuid')
    for data in get_psutil_cpu(hostUuid):
        monitor_stat(data)
