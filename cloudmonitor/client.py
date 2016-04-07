# -*- coding: utf-8 -*-

import time
from cloudmonitor.globalx import MONITOR_LOOP_INTERVAL

from cloudmonitor.static.host import start
from cloudmonitor.producer.cpu import pStatCpu
from cloudmonitor.consumer.cpu import cStatCpu
from cloudmonitor.producer.mem import pStatMem
from cloudmonitor.consumer.mem import cStatMem

def main():

    hostUuid = start()    
    pStatCpu(hostUuid).start()
    cStatCpu().start()
    pStatMem(hostUuid).start()
    cStatMem().start()
    
    while True:
        time.sleep(MONITOR_LOOP_INTERVAL)
        
if __name__ == '__main__':
    main()
