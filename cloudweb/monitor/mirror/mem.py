# -*- coding: utf-8 -*-

from cloudweb.db.table.dynamic.stat_mem import Mem,insert_mem,update_mem
from cloudweb.db.table.dynamic.stat_mem import hid2attrs as MEMhid2attrs
from cloudweb.monitor.mirror.base import MirrorBase

class MirrorMem(MirrorBase):
    def __init__(self,db,hid):
        super(MirrorMem, self).__init__(db,hid)
        
    @property
    def hid2attrs(self):
        
        return MEMhid2attrs
    
    @property
    def getClass(self):
        
        return Mem
    
    @property
    def emptyObject(self):
        
        return {self.c.hid:self.hid,self.c.id:None,
                self.c.timestamp:None,self.c.total:None,
                self.c.avai:None,self.c.seq:None}
            
    def insert_db(self,attr):
        pass
        timestamp = attr.get(self.c.timestamp)
        total = attr.get(self.c.total)
        available = attr.get(self.c.avai)
        insert_mem(self.db, self.hid, timestamp, total,available,self.currentseq)
        
    def update_db(self,attr,mirror_attr):
        pass
    
        timestamp = attr.get(self.c.timestamp)
        total = attr.get(self.c.total)
        available = attr.get(self.c.avai)
        cid = mirror_attr.get(self.c.id)
        update_mem(self.db, cid, timestamp, total,available,self.currentseq)
    
    def update_mirror(self,attr,mirror_attr):
        pass
        timestamp = attr.get(self.c.timestamp)
        total = attr.get(self.c.total)
        available = attr.get(self.c.avai)
        mirror_attr.update({self.c.timestamp:timestamp,self.c.total:total,
                       self.c.avai:available,self.c.seq:self.currentseq})
        
