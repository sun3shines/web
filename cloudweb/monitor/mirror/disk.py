# -*- coding: utf-8 -*-

from cloudweb.db.table.dynamic.stat_disk import Disk,insert_disk,update_disk
from cloudweb.db.table.dynamic.stat_disk import hid2attrs as DISKhid2attrs
from cloudweb.monitor.mirror.base import MirrorBase

class MirrorDisk(MirrorBase):
    def __init__(self,db,hid):
        super(MirrorDisk, self).__init__(db,hid)
        
    @property
    def hid2attrs(self):
        
        return DISKhid2attrs
    
    @property
    def getClass(self):
        
        return Disk
    
    @property
    def emptyObject(self):
        
        return {self.c.hid:self.hid,self.c.id:None,
                self.c.timestamp:None,self.c.disk_read_per_sec:None,
                self.c.disk_write_per_sec:None,self.c.seq:None}
            
    def insert_db(self,attr):
        print 'disk currentseq',self.currentseq
        print 'disk currentindex',self.currentindex
        timestamp = attr.get(self.c.timestamp)
        disk_read_per_sec = attr.get(self.c.disk_read_per_sec)
        disk_write_per_sec = attr.get(self.c.disk_write_per_sec)
        insert_disk(self.db, self.hid, timestamp, disk_read_per_sec,
                    disk_write_per_sec,self.currentseq)
        
    def update_db(self,attr,mirror_attr):
        pass
        print 'disk currentseq',self.currentseq   
        print 'disk currentindex',self.currentindex 
        timestamp = attr.get(self.c.timestamp)
        disk_read_per_sec = attr.get(self.c.disk_read_per_sec)
        disk_write_per_sec = attr.get(self.c.disk_write_per_sec)
        cid = mirror_attr.get(self.c.id)
        update_disk(self.db, cid, timestamp, disk_read_per_sec,
                    disk_write_per_sec,self.currentseq)
    
    def update_mirror(self,attr,mirror_attr):
        pass
        timestamp = attr.get(self.c.timestamp)
        disk_read_per_sec = attr.get(self.c.disk_read_per_sec)
        disk_write_per_sec = attr.get(self.c.disk_write_per_sec)
        mirror_attr.update({self.c.timestamp:timestamp,self.c.disk_read_per_sec:disk_read_per_sec,
                            self.c.disk_write_per_sec:disk_write_per_sec,self.c.seq:self.currentseq})
        
