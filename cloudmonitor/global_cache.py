# -*- coding: utf-8 -*-

import Queue
from cloudcommon.advanced.locklist import lockList

cpuQueue = Queue.Queue(1000)
memQueue = Queue.Queue(1000)
diskQueue = Queue.Queue(1000)
netQueue = Queue.Queue(1000)
storageQueue = Queue.Queue(1000)

MONITOR_DISK_PROCESS = lockList()