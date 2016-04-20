# -*- coding: utf-8 -*-

class Host:
    def __init__(self):
        
        self.table = 'host'
        self.id = 'id'
        self.name = 'name'
        self.uuid = 'uuid'
        self.product = 'product'
        self.manufacturer = 'manufacturer'
        self.version = 'version'
        self.serial = 'serial'
        self.asset_tag = 'asset_tag'
        self.available = 'available'
        
        
def insert_host(db,name,uuid,product,manuf,ver,serial,tag,avai):
    
    h = Host()
    keys = [h.name,h.uuid,h.product,h.manufacturer,
            h.version,h.serial,h.asset_tag,h.available]
    vals = [name,uuid,product,manuf,ver,serial,tag,avai]
    return db.insert(keys,vals,h.table)

def fetch_host(db,uuid=None):
    h = Host()
    attrs = [h.id,h.name,h.uuid,h.product,h.manufacturer,
            h.version,h.serial,h.asset_tag,h.available]
    
    c = {}
    if uuid:
        c = {h.uuid:uuid}
    return db.select(attrs,h.table,c)

def update_host(db,hid,updateattrs):
    
    h = Host()
    d = {}
    d.update(updateattrs)
    return db.update(d,h.table,{h.id:hid})

def uuid2attrs(db,uuid):
    
    h = Host()
    attrs = {}
    datas = fetch_host(db, uuid)
    if datas:
        data = datas[0]
        attrs[h.id] = data[0]
        attrs[h.name] = data[1]
        attrs[h.uuid] = data[2]
        attrs[h.product] = data[3]
        attrs[h.manufacturer] = data[4]
        attrs[h.version] = data[5]
        attrs[h.serial] = data[6]
        attrs[h.asset_tag] = data[7]
        attrs[h.available] = data[8]
        
    return attrs

def uuid2hostid(db,uuid):    
    return uuid2attrs(db, uuid).get('id')

def queryattrs(db):
    
    h = Host()
    attrss = []
    datas = fetch_host(db)
    
    for data in datas:
        attrs = {}
        attrs[h.id] = data[0]
        attrs[h.name] = data[1]
        attrs[h.uuid] = data[2]
        attrs[h.product] = data[3]
        attrs[h.manufacturer] = data[4]
        attrs[h.version] = data[5]
        attrs[h.serial] = data[6]
        attrs[h.asset_tag] = data[7]
        attrs[h.available] = data[8]
        attrss.append(attrs)
    return attrss
    
def puth(db,uuid,attrs):
    h = Host()
    dbattrs = uuid2attrs(db, uuid)
    if not dbattrs:
        name = attrs.get(h.name,'')
        uuid = attrs.get(h.uuid)
        product = attrs.get(h.product,'')
        manuf = attrs.get(h.manufacturer,'')
        ver = attrs.get(h.version,'')
        serial = attrs.get(h.serial,'')
        tag = attrs.get(h.asset_tag,'')
        avai = 'enable'
        return insert_host(db, name, uuid, product, manuf, ver, serial, tag, avai)
    
    d = {}
    for key in attrs:
        if dbattrs[key] != attrs.get(key,''):
            d[key] = attrs.get(key,'')
    if d:
        return update_host(db, dbattrs[h.id],d)
    return True,''
