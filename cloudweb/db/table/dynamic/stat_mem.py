# -*- coding: utf-8 -*-

class Mem:
    def __init__(self):
        self.table = 'stat_mem'
        self.id = 'id'
        self.hid = 'host_id'
        self.timestamp = 'timestamp'
        self.total = 'total'
        self.avai = 'available'
        self.seq = 'seq'
        
        
def insert_mem(db,hid,timestamp,total,avai,seq):
    
    m = Mem()
    keys = [m.hid,m.timestamp,m.total,m.avai,m.seq]
    vals = [hid,timestamp,total,avai,seq]
    return db.insert(keys,vals,m.table)

def update_mem(db,mid,timestamp,total,avai,seq):
    m = Mem()
    d = {}
    d.update({m.timestamp:timestamp,m.total:total,m.avai:avai,m.seq:seq})
    return db.update(d,m.table,{m.id:mid})

def fetch_mem(db,hid):
    m = Mem()
    attrs = [m.id,m.hid,m.timestamp,m.total,m.avai,m.seq]
    cond = {m.hid:hid}
    return db.select(attrs,m.table,cond)

def hid2attrs(db,hid):
    attrs = []
    m = Mem()
    datas = fetch_mem(db, hid)
    truncated =  datas
    for data in truncated:
        attr = {}
        attr[m.id] = data[0]
        attr[m.hid] = data[1]
        attr[m.timestamp] = data[2]
        attr[m.total] = data[3]
        attr[m.avai] = data[4]
        attr[m.seq] = data[5]
        attrs.append(attr)
    return attrs

def getLatesMem(db,hid):
    
    m = Mem()
        
    cStr = 'select max(b.seq) from stat_mem as b where a.host_id = b.host_id'
    sqlStr = 'select * from stat_mem as a where seq=(%s) and host_id=%s;' % (cStr,str(hid))
    datas = db.getDataList(sqlStr)

    attrs = []
    for data in datas:
        attr = {}
        attr[m.id] = data[0]
        attr[m.hid] = data[1]
        attr[m.timestamp] = data[2]
        attr[m.total] = data[3]
        attr[m.avai] = data[4]
        attr[m.seq] = data[5]
        attrs.append(attr)
    return attrs

