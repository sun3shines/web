# -*- coding: utf-8 -*-

import time
from cloudmonitor.globalx import MONITOR_LOOP_INTERVAL

from cloudmonitor.static.host import start
from cloudmonitor.producer.cpu import pStatCpu
from cloudmonitor.consumer.cpu import cStatCpu
from cloudmonitor.producer.mem import pStatMem
from cloudmonitor.consumer.mem import cStatMem
from cloudmonitor.producer.storage import pStatStorage
from cloudmonitor.consumer.storage import cStatStorage
from cloudmonitor.producer.net import pStatNet
from cloudmonitor.consumer.net import cStatNet
from cloudmonitor.producer.disk import pStatDisk
from cloudmonitor.consumer.disk import cStatDisk
from cloudmonitor.process.filter import ProcessFilter


def main():
    hostUuid = start()    
    ProcessFilter().start()
    
    pStatCpu(hostUuid).start()
    cStatCpu().start()
    pStatMem(hostUuid).start()
    cStatMem().start()
    pStatStorage(hostUuid).start()
    cStatStorage().start()
    pStatNet(hostUuid).start()
    cStatNet().start()
    pStatDisk(hostUuid).start()
    cStatDisk().start()
    
    while True:
        time.sleep(MONITOR_LOOP_INTERVAL)
        
if __name__ == '__main__':
    main()
