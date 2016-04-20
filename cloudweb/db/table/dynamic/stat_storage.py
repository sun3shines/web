# -*- coding: utf-8 -*-

class Storage:
    def __init__(self):
        self.table = 'stat_storage'
        self.id = 'id'
        self.hid = 'host_id'
        self.timestamp = 'timestamp'
        self.uuid = 'uuid'
        self.path = 'path'
        self.total = 'total'
        self.used = 'used'
        self.free = 'free'
        self.avai = 'available'
        self.seq = 'seq'
        
        
def insert_storage(db,hid,timestamp,uuid,path,total,used,free,avai,seq):
    
    s = Storage()
    keys = [s.hid,s.timestamp,s.uuid,s.path,s.total,s.used,s.free,s.avai,s.seq]
    vals = [hid,timestamp,uuid,path,total,used,free,avai,seq]
    return db.insert(keys,vals,s.table)

def update_storage(db,sid,timestamp,uuid,path,total,used,free,avai,seq):
    s = Storage()
    d = {}
    d.update({s.timestamp:timestamp,s.uuid:uuid,s.path:path,s.total:total,
              s.used:used,s.free:free,s.avai:avai,s.seq:seq})
    return db.update(d,s.table,{s.id:sid})

def fetch_storage(db,hid):
    s = Storage()
    attrs = [s.id,s.hid,s.timestamp,s.uuid,s.path,
             s.total,s.used,s.free,s.avai,s.seq]
    cond = {s.hid:hid}
    return db.select(attrs,s.table,cond)

def hid2attrs(db,hid):
    attrs = []
    s = Storage()
    datas = fetch_storage(db, hid)
    truncated =  datas
    for data in truncated:
        attr = {}
        attr[s.id] = data[0]
        attr[s.hid] = data[1]
        attr[s.timestamp] = data[2]
        attr[s.uuid] = data[3]
        attr[s.path] = data[4]
        attr[s.total] = data[5]
        attr[s.used] = data[6]
        attr[s.free] = data[7]
        attr[s.avai] = data[8]
        attr[s.seq] = data[9]
        attrs.append(attr)
    return attrs

def query_lates_storage(db,hid):
    attrs = hid2attrs(db, hid)
    
