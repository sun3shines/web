# -*- coding: utf-8 -*-

import threading
from cloudweb.monitor.globalx import GlobalQueue
from cloudweb.db.table.static.host import uuid2hostid
from cloudweb.monitor.mirror.net import MirrorNet

class StatNet(threading.Thread):
    def __init__(self,db,hostUuid):
        threading.Thread.__init__(self)
        self.db = db
        self.hostUuid = hostUuid
        
    def run(self):
        q = GlobalQueue.get(self.hostUuid).get('statNet')
        hostid = uuid2hostid(self.db, self.hostUuid)
        m = MirrorNet(self.db,hostid)
        while True:
            attr = q.get()
            m.append(attr)
