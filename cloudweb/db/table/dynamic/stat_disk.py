# -*- coding: utf-8 -*-

class Disk:
    def __init__(self):
        self.table = 'stat_disk'
        self.id = 'id'
        self.hid = 'host_id'
        self.timestamp = 'timestamp'
        self.disk_read_per_sec = 'disk_read_per_sec'
        self.disk_write_per_sec = 'disk_write_per_sec'
        self.seq = 'seq'
        
        
def insert_disk(db,hid,timestamp,disk_read_per_sec,disk_write_per_sec,seq):
    
    d = Disk()
    keys = [d.hid,d.timestamp,d.disk_read_per_sec,d.disk_write_per_sec,d.seq]
    vals = [hid,timestamp,disk_read_per_sec,disk_write_per_sec,seq]
    return db.insert(keys,vals,d.table)

def update_disk(db,mid,timestamp,disk_read_per_sec,disk_write_per_sec,seq):
    d = Disk()
    dvs = {}
    dvs.update({d.timestamp:timestamp,d.disk_read_per_sec:disk_read_per_sec,d.disk_write_per_sec:disk_write_per_sec,d.seq:seq})
    return db.update(dvs,d.table,{d.id:mid})

def fetch_disk(db,hid):
    d = Disk()
    attrs = [d.id,d.hid,d.timestamp,d.disk_read_per_sec,d.disk_write_per_sec,d.seq]
    cond = {d.hid:hid}
    return db.select(attrs,d.table,cond)

def hid2attrs(db,hid):
    attrs = []
    d = Disk()
    datas = fetch_disk(db, hid)
    truncated =  datas
    for data in truncated:
        attr = {}
        attr[d.id] = data[0]
        attr[d.hid] = data[1]
        attr[d.timestamp] = data[2]
        attr[d.disk_read_per_sec] = data[3]
        attr[d.disk_write_per_sec] = data[4]
        attr[d.seq] = data[5]
        attrs.append(attr)
    return attrs

