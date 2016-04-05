# -*- coding: utf-8 -*-

class Disk:
    def __init__(self):
        self.table = 'host_disk'
        self.hid = 'host_id'
        self.id = 'id'
        self.name = 'logicalname'
        self.desc = 'description'
        self.product = 'product'
        self.vendor = 'vendor'
        self.phyid = 'physical_id'
        self.bus = 'bus_info'
        self.ver = 'version'
        self.serial = 'serial'
        self.size = 'size'
        
def insert_disk(db,hid,name,desc,product,vendor,phyid,bus,ver,serial,size):

    if not serial:
        return False,'serial error'
        
    d = Disk()
    keys = [d.hid,d.name,d.desc,d.product,d.vendor,d.phyid,d.bus,d.ver,d.serial,d.size]
    vals = [hid,name,desc,product,vendor,phyid,bus,ver,serial,size]
    return db.insert(keys,vals,d.table)

def delete_disk(db,did):
    
    d = Disk()
    return db.delete(d.table,{d.id:str(did)})

def fetch_disk(db,hid):
    
    d = Disk()
    attrs = [d.id,d.hid,d.name,d.desc,d.product,d.vendor,d.phyid,d.bus,d.ver,d.serial,d.size]
    c = {d.hid:hid}
    return db.select(attrs,d.table,c)    

def hid2attrs(db,hid):
    d = Disk()
    attrs = []
    datas = fetch_disk(db, hid)
    for data in datas:
        attr = {}
        attr[d.id] = data[0]
        attr[d.hid] = data[1]
        attr[d.name] = data[2]
        attr[d.desc] = data[3]
        attr[d.product] = data[4]
        attr[d.vendor] = data[5]
        attr[d.phyid] = data[6]
        attr[d.bus] = data[7]
        attr[d.ver] = data[8]
        attr[d.serial] = data[9]
        attr[d.size] = data[10]
        
        attrs.append(attr)
        
    return attrs

def putds(db,hid,attrs):
    
    d = Disk()
    dbattrs = hid2attrs(db, hid)
    
    for dbattr in dbattrs:
        dbserial = dbattr.get(d.serial)
        dbid = dbattr.get(d.id)
        exists = False
        for attr in attrs:
            if dbserial == attr.get(d.serial):
                exists = True
                break
        if not exists:
            delete_disk(db, dbid)
            
    for attr in attrs:
        exists = False
        serial = attr.get(d.serial)
        for dbattr in dbattrs:
            if serial == dbattr.get(d.serial):
                exists = True
                break
            
        if exists:
            continue
        
        name = attr.get(d.name)
        desc = attr.get(d.desc)
        product = attr.get(d.product)
        vendor = attr.get(d.vendor)
        phyid = attr.get(d.phyid)
        bus = attr.get(d.bus)
        ver = attr.get(d.ver)
        serial = attr.get(d.serial)
        size = attr.get(d.size)
        insert_disk(db,hid,name,desc,product,vendor,phyid,bus,ver,serial,size)
        
            
        
