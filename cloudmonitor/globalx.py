# -*- coding: utf-8 -*-

import Queue

cpuQueue = Queue.Queue(1000)
memQueue = Queue.Queue(1000)
diskQueue = Queue.Queue(1000)
netQueue = Queue.Queue(1000)
storageQueue = Queue.Queue(1000)

HOST_PATH = 'hostUuid'

MONITOR_SERVER_HOST = '192.168.36.3'
MONITOR_SERVER_PORT = 7013
HTTP_TIMEOUT = 100