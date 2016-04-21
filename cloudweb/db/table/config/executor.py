# -*- coding: utf-8 -*-

class Executor:
    def __init__(self):
        self.table = 'config_executor'
        self.id = 'id'
        self.name = 'name'
        self.uuid = 'uuid'
        self.inet = 'inet'
        self.avai = 'available'
        
def insert_executor(db,name,uuid,inet,avai):
    
    e = Executor()
    
    keys = [e.name,e.uuid,e.inet,e.avai]
    vals = [name,uuid,inet,avai]
    return db.insert(keys,vals,e.table)

def fetch_executor(db,uuid=None,inet=None):
    
    e = Executor()
    
    attrs = [e.id,e.name,e.uuid,e.inet,e.avai]
    c = {}
    if uuid:
        c.update({e.uuid:uuid})
    if inet:
        c.update({e.inet:inet})
        
    return db.select(attrs,e.table,c)

def ip2attrs(db,inet):
    
    attrs = []
    e = Executor()
    datas = fetch_executor(db, None,inet =inet)

    truncated =  datas
    for data in truncated:
        attr = {}
        attr[e.id] = data[0]
        attr[e.name] = data[1]
        attr[e.uuid] = data[2]
        attr[e.inet] = data[3]
        attr[e.avai] = data[4]
        attrs.append(attr)
    return attrs

def uuid2attrs(db,uuid):
    
    attrs = []
    e = Executor()
    datas = fetch_executor(db, uuid=uuid)

    truncated =  datas
    for data in truncated:
        attr = {}
        attr[e.id] = data[0]
        attr[e.name] = data[1]
        attr[e.uuid] = data[2]
        attr[e.inet] = data[3]
        attr[e.avai] = data[4]
        attrs.append(attr)
    return attrs

def query_all_executor(db):
    
    attrs = []
    e = Executor()
    datas = fetch_executor(db)

    truncated =  datas
    for data in truncated:
        attr = {}
        attr[e.name] = data[1]
        attr[e.uuid] = data[2]
        attr[e.inet] = data[3]
        attr[e.avai] = data[4]
        attrs.append(attr)
    return attrs    

