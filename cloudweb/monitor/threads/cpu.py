# -*- coding: utf-8 -*-

import threading
from cloudweb.monitor.globalx import GlobalQueue
from cloudweb.db.table.static.host import uuid2hostid
from cloudweb.monitor.mirror.cpu import MirrorCpu

class StatCpu(threading.Thread):
    def __init__(self,db,hostUuid):
        threading.Thread.__init__(self)
        self.db = db
        self.hostUuid = hostUuid
        
    def run(self):
        q = GlobalQueue.get(self.hostUuid).get('statCpu')
        hostid = uuid2hostid(self.db, self.hostUuid)
        m = MirrorCpu(self.db,hostid)
        while True:
#            import pdb;pdb.set_trace()
            attr = q.get()
            print attr
            print 'in thread'
            m.append(attr)
