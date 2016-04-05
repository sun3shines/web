# -*- coding: utf-8 -*-

class Memory:
    def __init__(self):
        self.table = 'host_mem'
        self.hid = 'host_id'
        self.id = 'id'
        self.total_width = 'total_width'
        self.data_width = 'data_width'
        self.size = 'size'
        self.form_factor = 'form_factor'
        self.speed = 'speed'
        self.manuf = 'manufacturer'
        self.serial = 'serial'
        self.tag = 'asset_tag'
        self.part_number = 'part_number'
        
def insert_mem(db,hid,total_width,data_width,size,
               form_factor,speed,manuf,serial,tag,part_number):
    
    if not serial:
        return False,'serial error'
    
    m = Memory()
    keys = [m.hid,m.total_width,m.data_width,m.size,m.form_factor,
            m.speed,m.manuf,m.serial,m.tag,m.part_number]
    vals = [hid,total_width,data_width,size,form_factor,
            speed,manuf,serial,tag,part_number]
    
    return db.insert(keys,vals,m.table)

def delete_mem(db,mid):
    
    m = Memory()
    return db.delete(m.table,{m.id:str(mid)})

def fetch_mem(db,hid):
    
    m = Memory()
    attrs = [m.id,m.hid,m.total_width,m.data_width,m.size,
             m.form_factor,m.speed,m.manuf,m.serial,m.tag,m.part_number]
    c = {m.hid:hid}
    return db.select(attrs,m.table,c)

def hid2attrs(db,hid):
    m = Memory()
    attrs = []
    datas = fetch_mem(db, hid)
    for data in datas:
        attr = {}
        attr[m.id] = data[0]
        attr[m.hid] = data[1]
        attr[m.total_width] = data[2]
        attr[m.data_width] = data[3]
        attr[m.size] = data[4]
        attr[m.form_factor] = data[5]
        attr[m.speed] = data[6]
        attr[m.manuf] = data[7]
        attr[m.serial] = data[8]
        attr[m.tag] = data[9]
        attr[m.part_number] = data[10]
        
        attrs.append(attr)
        
    return attrs


def putms(db,hid,attrs):
    
    m = Memory()
    dbattrs = hid2attrs(db, hid)
    
    for dbattr in dbattrs:
        dbserial = dbattr.get(m.serial)
        dbid = dbattr.get(m.id)
        exists = False
        for attr in attrs:
            if dbserial == attr.get(m.serial):
                exists = True
                break
        if not exists:
            delete_mem(db, dbid)
            
    for attr in attrs:
        exists = False
        serial = attr.get(m.serial)
        for dbattr in dbattrs:
            if serial == dbattr.get(m.serial):
                exists = True
                break
            
        if exists:
            continue
        
        total_width = attr.get(m.total_width,'')
        data_width = attr.get(m.data_width,'')
        size = attr.get(m.size,'')
        form_factor = attr.get(m.form_factor,'')
        speed = attr.get(m.speed,'')
        manuf = attr.get(m.manuf,'')
        serial = attr.get(m.serial)
        tag = attr.get(m.tag,'')
        part_number = attr.get(m.part_number,'')
        insert_mem(db, hid, total_width, data_width, size, form_factor,
                   speed, manuf, serial, tag, part_number)
            
        

