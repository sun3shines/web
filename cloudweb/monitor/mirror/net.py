# -*- coding: utf-8 -*-

from cloudweb.db.table.dynamic.stat_net import Network, update_net,insert_net
from cloudweb.db.table.dynamic.stat_net import hid2attrs as NEThid2attrs
from cloudweb.monitor.mirror.base import MirrorBase

class MirrorNet(MirrorBase):
    def __init__(self,db,hid):
        super(MirrorNet, self).__init__(db,hid)
        
    @property
    def hid2attrs(self):
        
        return NEThid2attrs
    
    @property
    def getClass(self):
        
        return Network
    
    @property
    def emptyObject(self):
        
        return {self.c.hid:self.hid,self.c.id:None,
                self.c.timestamp:None,self.c.bytes_sent_per_sec:None,
                self.c.bytes_recv_per_sec:None,self.c.packet_recv_per_sec:None,
                self.c.seq:None}
            
    def insert_db(self,attr):
        pass
        timestamp = attr.get(self.c.timestamp)
        bytes_sent_per_sec = attr.get(self.c.bytes_sent_per_sec)
        bytes_recv_per_sec = attr.get(self.c.bytes_recv_per_sec)
        packet_send_per_sec = attr.get(self.c.packet_send_per_sec)
        packet_recv_per_sec = attr.get(self.c.packet_recv_per_sec)
        insert_net(self.db, self.hid, timestamp, bytes_sent_per_sec,bytes_recv_per_sec,
                   packet_send_per_sec,packet_recv_per_sec,self.currentseq)
        
    def update_db(self,attr,mirror_attr):
        pass
    
        timestamp = attr.get(self.c.timestamp)
        bytes_sent_per_sec = attr.get(self.c.bytes_sent_per_sec)
        bytes_recv_per_sec = attr.get(self.c.bytes_recv_per_sec)
        packet_send_per_sec = attr.get(self.c.packet_send_per_sec)
        packet_recv_per_sec = attr.get(self.c.packet_recv_per_sec)
        
        cid = mirror_attr.get(self.c.id)
        update_net(self.db, cid, timestamp, bytes_sent_per_sec,bytes_recv_per_sec,
                   packet_send_per_sec,packet_recv_per_sec,self.currentseq)
    
    def update_mirror(self,attr,mirror_attr):
        pass
        timestamp = attr.get(self.c.timestamp)
        bytes_sent_per_sec = attr.get(self.c.bytes_sent_per_sec)
        bytes_recv_per_sec = attr.get(self.c.bytes_recv_per_sec)
        packet_send_per_sec = attr.get(self.c.packet_send_per_sec)
        packet_recv_per_sec = attr.get(self.c.packet_recv_per_sec)
        mirror_attr.update({self.c.timestamp:timestamp,self.c.bytes_sent_per_sec:bytes_sent_per_sec,
                            self.c.bytes_recv_per_sec:bytes_recv_per_sec,
                            self.c.packet_send_per_sec:packet_send_per_sec,
                            self.c.packet_recv_per_sec:packet_recv_per_sec,self.c.seq:self.currentseq})
        
