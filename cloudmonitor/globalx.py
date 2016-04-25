# -*- coding: utf-8 -*-

from cloudlib.globalx.config import MO_HTTP_TIMEOUT,MO_MONITOR_SERVER_HOST,MO_MONITOR_SERVER_PORT

MONITOR_SERVER_HOST = MO_MONITOR_SERVER_HOST
MONITOR_SERVER_PORT = MO_MONITOR_SERVER_PORT
HTTP_TIMEOUT = MO_HTTP_TIMEOUT

MONITOR_CONNECT_INTERVAL =  10
MONITOR_LOOP_INTERVAL = 30

PSUTIL_CPU_INTERVAL = 2 
PSUTIL_MEM_INTERVAL = 2
PSUTIL_DISK_INTERVAL = 2 
PSUTIL_NET_INTERVAL = 2
PSUTIL_STORAGE_INTERVAL = 30
PSUTIL_PROCESS_INTERVAL = 5
PSUTIL_SERVICE_INTERVAL = 5 

MONITOR_ALLOWD_FSTYPE = ['ext4','cifs','nfs']

CLOUD_CMDLINES = [('/usr/bin/python','/usr/bin/swift-account-server'),
                  ('/usr/bin/python','/usr/bin/swift-container-server'),
                  ('/usr/bin/python','/usr/bin/swift-object-server'),
                  ('/usr/bin/python','/usr/bin/cloud-web-server'),
                  ('/usr/bin/python','/usr/bin/cloud-monitor-server'),
                  ('python','psutil_io.py')]

SERVICE_CMDLINE = {'proxy':('/usr/bin/python','/usr/bin/swift-proxy-server'),
                   'account':('/usr/bin/python','/usr/bin/swift-account-server'),
                   'container':('/usr/bin/python','/usr/bin/swift-container-server'),
                   'object':('/usr/bin/python','/usr/bin/swift-object-server'),
                   'cloud-web':('/usr/bin/python','/usr/bin/cloud-web-server'),
                   'cloud-monitor':('/usr/bin/python','/usr/bin/cloud-monitor-server')}
