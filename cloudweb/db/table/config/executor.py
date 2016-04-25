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

def del_executor(db,eid):
    e = Executor()
    return db.delete(e.table,{e.id:str(eid)})

def fetch_executor(db,inet=None,uuid=None):
    
    e = Executor()
    
    attrs = [e.id,e.name,e.uuid,e.inet,e.avai]
    c = {}
    if uuid:
        c.update({e.uuid:uuid})
    if inet:
        c.update({e.inet:inet})
        
    return db.select(attrs,e.table,c)

def query_all_executor(db,inet=None,uuid=None):
    
    attrs = []
    e = Executor()
    datas = fetch_executor(db,inet,uuid)

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

def ip2attrs(db,inet):
    
    datas =  query_all_executor(db, inet=inet)
    if datas:
        return datas[0]
    else:
        return {}

def uuid2attrs(db,uuid):
    
    datas = query_all_executor(db, inet=None,uuid=uuid)
    if datas:
        return datas[0]
    else:
        return {}
    
