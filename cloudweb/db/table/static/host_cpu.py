# -*- coding: utf-8 -*-

class Cpu:
    def __init__(self):
        self.table = 'host_cpu'
        self.hid = 'host_id'
        self.id = 'id'
        self.desc = 'description'
        self.product = 'product'
        self.vendor = 'vendor'
        self.phyid = 'physical_id'
        self.bus = 'bus_info'
        self.version = 'version'
        self.size = 'size'
        self.capacity = 'capacity'
        self.width = 'width'
        self.clock = 'clock'
        self.cores = 'cores'
        self.enabledcores = 'enabledcores'
        self.threads = 'threads'
        
def insert_cpu(db,hid,desc,product,vendor,phyid,bus,version,
               size,capacity,width,clock,cores,enabledcores,threads):
    
    c = Cpu()
    keys = [c.hid,c.desc,c.product,c.vendor,c.phyid,c.bus,c.version,
            c.size,c.capacity,c.width,c.clock,c.cores,c.enabledcores,c.threads]
    vals = [hid,desc,product,vendor,phyid,bus,version,
            size,capacity,width,clock,cores,enabledcores,threads]
    return db.insert(keys,vals,c.table)

def fetch_cpu(db,hid):
    c = Cpu()
    attrs = [c.hid,c.id,c.desc,c.product,c.vendor,c.phyid,c.bus,c.version,
             c.size,c.capacity,c.width,c.clock,c.cores,c.enabledcores,c.threads]
    cond = {c.hid:hid}
    return db.select(attrs,c.table,cond)

def update_cpu(db,hid,updateattrs):
    c = Cpu()
    d = {}
    d.update(updateattrs)
    return db.update(d,c.table,{c.hid:hid})

def hid2attrs(db,hid):
    c = Cpu()
    attrs = {}
    datas = fetch_cpu(db, hid)
    if datas:
        data = datas[0]
        attrs[c.id] = data[0]
        attrs[c.hid] = data[1]
        attrs[c.desc] = data[2]
        attrs[c.product] = data[3]
        attrs[c.vendor] = data[4]
        attrs[c.phyid] = data[5]
        attrs[c.bus] = data[6]
        attrs[c.version] = data[7]
        attrs[c.size] = data[8]
        attrs[c.capacity] = data[9]
        attrs[c.width] = data[10]
        attrs[c.clock] = data[11]
        attrs[c.cores] = data[12]
        attrs[c.enabledcores] = data[13]
        attrs[c.threads] = data[14]
        
    return attrs

def putc(db,hid,attrs):
    c = Cpu()
    dbattrs = hid2attrs(db, hid)
    if not dbattrs:
        host_id = hid
        desc = attrs.get(c.desc,'')
        product = attrs.get(c.product,'')
        vendor = attrs.get(c.vendor,'')
        phyid = attrs.get(c.phyid,'')
        bus = attrs.get(c.bus,'')
        ver = attrs.get(c.version,'')
        size = attrs.get(c.size,'')
        capacity = attrs.get(c.capacity,'')
        width = attrs.get(c.width,'')
        clock = attrs.get(c.clock,'')
        cores = attrs.get(c.cores,'')
        enabledcores = attrs.get(c.enabledcores,'')
        threads = attrs.get(c.threads,'')
        
        return insert_cpu(db, host_id,desc,product,vendor,phyid,bus,ver,
                          size,capacity,width,clock,cores,enabledcores,threads)
    
    d = {}
    for key in attrs:
        if dbattrs[key] != attrs.get(key,''):
            d[key] = attrs.get(key,'')
    if d:
        return update_cpu(db, dbattrs[c.hid],d)
    return True,''
