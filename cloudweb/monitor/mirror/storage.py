# -*- coding: utf-8 -*-

from cloudweb.db.table.dynamic.stat_storage import Storage, update_storage,insert_storage
from cloudweb.db.table.dynamic.stat_storage import hid2attrs as STORAGEhid2attrs
from cloudweb.monitor.mirror.base import MirrorBase

class MirrorStorage(MirrorBase):
    def __init__(self,db,hid):
        super(MirrorStorage, self).__init__(db,hid)
        
    @property
    def hid2attrs(self):
        
        return STORAGEhid2attrs
    
    @property
    def getClass(self):
        
        return Storage
    
    @property
    def emptyObject(self):
        
        return {self.c.hid:self.hid,self.c.id:None,
                self.c.timestamp:None,self.c.uuid:None,self.c.path:None,self.c.total:None,
                self.c.used:None,self.c.free:None,self.c.avai:None,self.c.seq:None}
            
    def insert_db(self,attr):
        pass
        timestamp = attr.get(self.c.timestamp)
        uuid = attr.get(self.c.uuid)
        path = attr.get(self.c.path)
        total = attr.get(self.c.total)
        used = attr.get(self.c.used)
        free = attr.get(self.c.free)
        available = attr.get(self.c.avai)
        insert_storage(self.db, self.hid, timestamp, uuid,path,
                       total,used,free,available,self.currentseq)
        
    def update_db(self,attr,mirror_attr):
        pass
    
        timestamp = attr.get(self.c.timestamp)
        uuid = attr.get(self.c.uuid)
        path = attr.get(self.c.path)
        total = attr.get(self.c.total)
        used = attr.get(self.c.used)
        free = attr.get(self.c.free)
        available = attr.get(self.c.avai)
        
        cid = mirror_attr.get(self.c.id)
        update_storage(self.db, cid, timestamp, uuid,path,
                       total,used,free,available,self.currentseq)
    
    def update_mirror(self,attr,mirror_attr):
        timestamp = attr.get(self.c.timestamp)
        uuid = attr.get(self.c.uuid)
        path = attr.get(self.c.path)
        total = attr.get(self.c.total)
        used = attr.get(self.c.used)
        free = attr.get(self.c.free)
        available = attr.get(self.c.avai)
        
        mirror_attr.update({self.c.timestamp:timestamp,self.c.uuid:uuid,self.c.path:path,self.c.total:total,
                            self.c.used:used,self.c.free:free,
                            self.c.avai:available,self.c.seq:self.currentseq})
        
