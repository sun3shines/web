# -*- coding: utf-8 -*-

from cloudweb.db.table.dynamic.stat_cpu import Cpu, update_cpu,insert_cpu
from cloudweb.db.table.dynamic.stat_cpu import hid2attrs as CPUhid2attrs
from cloudweb.monitor.mirror.base import MirrorBase

class MirrorCpu(MirrorBase):
    def __init__(self,db,hid):
        super(MirrorCpu, self).__init__(db,hid)
        
    @property
    def hid2attrs(self):
        
        return CPUhid2attrs
    
    @property
    def getClass(self):
        
        return Cpu
    
    @property
    def emptyObject(self):
        
        return {self.c.hid:self.hid,self.c.id:None,
                self.c.timestamp:None,self.c.utilization:None,
                self.c.seq:None}
            
    def insert_db(self,attr):
        pass
        timestamp = attr.get(self.c.timestamp)
        utilization = attr.get(self.c.utilization)
        insert_cpu(self.db, self.hid, timestamp, utilization,self.currentseq)
        
    def update_db(self,attr,mirror_attr):
        pass
    
        timestamp = attr.get(self.c.timestamp)
        utilization = attr.get(self.c.utilization)
        cid = mirror_attr.get(self.c.id)
        update_cpu(self.db, cid, timestamp, utilization,self.currentseq)
    
    def update_mirror(self,attr,mirror_attr):
        pass
        timestamp = attr.get(self.c.timestamp)
        utilization = attr.get(self.c.utilization)
        mirror_attr.update({self.c.timestamp:timestamp,self.c.utilization:utilization,
                       self.c.seq:self.currentseq})
        
