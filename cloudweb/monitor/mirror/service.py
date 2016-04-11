# -*- coding: utf-8 -*-

from cloudweb.db.table.dynamic.stat_service import Service, update_service,insert_service
from cloudweb.db.table.dynamic.stat_service import hid2attrs as SERVICEhid2attrs
from cloudweb.monitor.mirror.base import MirrorBase

class MirrorService(MirrorBase):
    def __init__(self,db,hid):
        super(MirrorService, self).__init__(db,hid)
        
    @property
    def hid2attrs(self):
        
        return SERVICEhid2attrs
    
    @property
    def getClass(self):
        
        return Service
    
    @property
    def emptyObject(self):
        
        return {self.c.hid:self.hid,self.c.id:None,
                self.c.timestamp:None,self.c.name:None,self.c.cmdline:None,self.c.active_status:None,
                self.c.open_files:None,self.c.thread_num:None,
                self.c.net_connections:None,self.c.cpu_utilization:None,
                self.c.mem_utilization:None,self.c.avai:None,self.c.seq:None}
            
    def insert_db(self,attr):
        
        timestamp = attr.get(self.c.timestamp)
        name = attr.get(self.c.name)
        cmdline = attr.get(self.c.cmdline)
        active_status = attr.get(self.c.active_status)
        open_files = attr.get(self.c.open_files)
        net_connections = attr.get(self.c.net_connections)
        thread_num = attr.get(self.c.thread_num)
        cpu_utilization = attr.get(self.c.cpu_utilization)
        mem_utilization = attr.get(self.c.mem_utilization)
        
        available = attr.get(self.c.avai)
        insert_service(self.db, self.hid, timestamp, name,cmdline,active_status,
                       open_files,net_connections,thread_num,cpu_utilization,mem_utilization,
                       available,self.currentseq)
        
    def update_db(self,attr,mirror_attr):
        pass
    
        timestamp = attr.get(self.c.timestamp)
        name = attr.get(self.c.name)
        cmdline = attr.get(self.c.cmdline)
        active_status = attr.get(self.c.active_status)
        open_files = attr.get(self.c.open_files)
        net_connections = attr.get(self.c.net_connections)
        thread_num = attr.get(self.c.thread_num)
        cpu_utilization = attr.get(self.c.cpu_utilization)
        mem_utilization = attr.get(self.c.mem_utilization)
        available = attr.get(self.c.avai)
        
        cid = mirror_attr.get(self.c.id)
        update_service(self.db, cid, timestamp, name,cmdline,active_status,
                       open_files,net_connections,thread_num,cpu_utilization,mem_utilization,
                       available,self.currentseq)
    
    def update_mirror(self,attr,mirror_attr):
        timestamp = attr.get(self.c.timestamp)
        name = attr.get(self.c.name)
        cmdline = attr.get(self.c.cmdline)
        active_status = attr.get(self.c.active_status)
        open_files = attr.get(self.c.open_files)
        net_connections = attr.get(self.c.net_connections)
        thread_num = attr.get(self.c.thread_num)
        cpu_utilization = attr.get(self.c.cpu_utilization)
        mem_utilization = attr.get(self.c.mem_utilization)
        available = attr.get(self.c.avai)
        
        mirror_attr.update({self.c.timestamp:timestamp,self.c.name:name,self.c.cmdline:cmdline,
                            self.c.active_status:active_status,self.c.open_files:open_files,
                            self.c.net_connections:net_connections,self.c.thread_num:thread_num,
                            self.c.cpu_utilization:cpu_utilization,
                            self.c.mem_utilization:mem_utilization,self.c.avai:available,self.c.seq:self.currentseq})
        
