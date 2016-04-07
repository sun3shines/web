# -*- coding: utf-8 -*-

import threading
from cloudweb.monitor.globalx import GlobalQueue
from cloudweb.db.table.static.host import uuid2hostid
from cloudweb.monitor.mirror.disk import MirrorDisk
from cloudweb.db.table.lock.mysql import getdb

class StatDisk(threading.Thread):
    def __init__(self,hostUuid):
        threading.Thread.__init__(self)
        self.db = getdb()
        self.hostUuid = hostUuid
        
    def run(self):
        q = GlobalQueue.get(self.hostUuid).get('statDisk')
        hostid = uuid2hostid(self.db, self.hostUuid)
        m = MirrorDisk(self.db,hostid)
        while True:
            attr = q.get()
            m.append(attr)
