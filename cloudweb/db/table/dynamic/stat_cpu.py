# -*- coding: utf-8 -*-

class Cpu:
    def __init__(self):
        self.table = 'stat_cpu'
        self.hid = 'host_id'
        self.id = 'id'
        self.timestamp = 'timestamp'
        self.utilization = 'utilization'
        self.seq = 'seq'
        
def insert_cpu(db,hid,timestamp,utilization,seq):
    
    c = Cpu()
    keys = [c.hid,c.timestamp,c.utilization,c.seq]
    vals = [hid,timestamp,utilization,seq]
    return db.insert(keys,vals,c.table)

def update_cpu(db,cid,timestamp,utilization,seq):
    c = Cpu()
    d = {}
    d.update({c.timestamp:timestamp,c.utilization:utilization,c.seq:seq})
    return db.update(d,c.table,{c.id:cid})

def fetch_cpu(db,hid):
    c = Cpu()
    attrs = [c.id,c.hid,c.timestamp,c.utilization,c.seq]
    cond = {c.hid:hid}
    return db.select(attrs,c.table,cond)

def hid2attrs(db,hid):
    attrs = []
    c = Cpu()
    datas = fetch_cpu(db, hid)
#    truncated =  datas[-1000:]
    truncated =  datas
    for data in truncated:
        attr = {}
        attr[c.id] = data[0]
        attr[c.hid] = data[1]
        attr[c.timestamp] = data[2]
        attr[c.utilization] = data[3]
        attr[c.seq] = data[4]
        attrs.append(attr)
    return attrs
