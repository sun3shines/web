# -*- coding: utf-8 -*-

from cloudmonitor.http.api import monitor_start,monitor_stat
from cloudmonitor.static.host import get_host_static

if __name__ == '__main__':
    host_hw = get_host_static()
    monitor_start(host_hw)
    
