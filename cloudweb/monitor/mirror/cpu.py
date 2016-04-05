# -*- coding: utf-8 -*-

from cloudweb.db.table.dynamic.stat_cpu import hid2attrs,Cpu, update_cpu,\
    insert_cpu

class Cpu:
    def __init__(self,db,hid):
        self.db = db
        self.hid = hid
        self.currentindex = 0
        self.currentseq = 0
        self.l = []
        self.c = Cpu()
        self.load()
        
    def load(self):
        self.l = hid2attrs(self.db, self.hid)
        if 1000 == len(self.l):
            
            maxseq = -1 
            for attr in self.l:
                seq = float(attr[self.c.seq]) 
                if seq > maxseq:
                    maxseq = seq
                    self.currentindex = self.currentindex + 1
            self.currentseq = maxseq + 1
            
        else:
            self.currentindex = len(self.l)
            while len(self.l) < 1000:
                self.l.append({self.c.hid:self.hid,self.c.id:None,
                               self.c.timestamp:None,self.c.utilization:None,
                               self.c.seq:None})
            
    def append(self,attr):
        self.update(attr)
        self.currentindex = self.currentindex + 1
        self.currentseq = self.currentseq + 1
        if 1000 == self.currentindex:
            self.currentindex = 0
            self.l = hid2attrs(self.db, self.hid)
            
    def update(self,attr):
        dbattr = self.l[self.currentindex]
        timestamp = attr.get(self.c.timestamp)
        utilization = attr.get(self.c.utilization)
        
        if not dbattr.get(self.c.seq):
            insert_cpu(self.db, self.hid, timestamp, utilization,self.currentseq)
        else:
            cid = dbattr.get(self.c.id)
            update_cpu(self.db, cid, timestamp, utilization,self.currentseq)
            
        dbattr.update({self.c.timestamp:timestamp,self.c.utilization:utilization,
                       self.c.seq:self.currentseq})
    

    