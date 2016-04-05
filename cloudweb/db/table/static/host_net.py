# -*- coding: utf-8 -*-

class Netcard:
    def __init__(self):
        self.table = 'host_net'
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
        self.capacity = 'capacity'
        self.width = 'width'
        self.clock = 'clock'
        self.mtu = 'mtu'
        self.mac = 'mac'
        self.inet = 'inet'
        self.primary = 'is_primary'
        
def insert_net(db,hid,name,desc,product,vendor,phyid,bus,ver,
               serial,size,capacity,width,clock,mtu,mac,inet,primary):
    
    if not serial:
        return False,'serial error'
    n = Netcard()
    keys = [n.hid,n.name,n.desc,n.product,n.vendor,n.phyid,n.bus,n.ver,
            n.serial,n.size,n.capacity,n.width,n.clock,n.mtu,n.mac,n.inet,n.primary]
    
    vals = [hid,name,desc,product,vendor,phyid,bus,ver,
            serial,size,capacity,width,clock,mtu,mac,inet,primary]
    return db.insert(keys,vals,n.table)

def delete_net(db,nid):
    n = Netcard()
    return db.delete(n.table,{n.id:str(nid)})


def fetch_net(db,hid):
    n = Netcard()
    attrs = [n.id,n.hid,n.name,n.desc,n.product,n.vendor,n.phyid,n.bus,n.ver,
            n.serial,n.size,n.capacity,n.width,n.clock,n.mtu,n.mac,n.inet,n.primary]
    c = {n.hid:hid}
    return db.select(attrs,n.table,c)


def hid2attrs(db,hid):
    n = Netcard()
    attrs = []
    datas = fetch_net(db, hid)
    for data in datas:
        attr = {}
        attr[n.id] = data[0]
        attr[n.hid] = data[1]
        attr[n.name] = data[2]
        attr[n.desc] = data[3]
        attr[n.product] = data[4]
        attr[n.vendor] = data[5]
        attr[n.phyid] = data[6]
        attr[n.bus] = data[7]
        attr[n.ver] = data[8]
        attr[n.serial] = data[9]
        attr[n.size] = data[10]
        attr[n.capacity] = data[11]
        attr[n.width] = data[12]
        attr[n.clock] = data[13]
        attr[n.mtu] = data[14]
        attr[n.mac] = data[15]
        attr[n.inet] = data[16]
        attr[n.primary] = data[17]
        
        attrs.append(attr)
        
    return attrs

def putns(db,hid,attrs):
    
    n = Netcard()
    dbattrs = hid2attrs(db, hid)
    
    for dbattr in dbattrs:
        dbserial = dbattr.get(n.serial)
        dbid = dbattr.get(n.id)
        exists = False
        for attr in attrs:
            if dbserial == attr.get(n.serial):
                exists = True
                break
        if not exists:
            delete_net(db, dbid)
            
    for attr in attrs:
        exists = False
        serial = attr.get(n.serial)
        for dbattr in dbattrs:
            if serial == dbattr.get(n.serial):
                exists = True
                break
            
        if exists:
            continue
        
        name = attr.get(n.name)
        desc = attr.get(n.desc)
        product = attr.get(n.product)
        vendor = attr.get(n.vendor)
        phyid = attr.get(n.phyid)
        bus = attr.get(n.bus)
        ver = attr.get(n.ver)
        serial = attr.get(n.serial)
        size = attr.get(n.size)
        capacity = attr.get(n.capacity)
        width = attr.get(n.width)
        clock = attr.get(n.clock)
        mtu = attr.get(n.mtu)
        mac = attr.get(n.mac)
        inet = attr.get(n.inet)
        primary = attr.get(n.primary)
        insert_net(db,hid,name,desc,product,vendor,phyid,bus,ver,
               serial,size,capacity,width,clock,mtu,mac,inet,primary)
            
        