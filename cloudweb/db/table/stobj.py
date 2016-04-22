# -*- coding: utf-8 -*-

# fetch_one_path_id -> onepath2id

# fetch_path_id -> fullPath2id

# fetch_account_id -> account2id account.py

# account_exists -> account_exists account.py

# insert_account -> insert_account account.py

# fetch_one_attrs -> id2attrs

# fetch_path_attrs -> fullPath2attrs

# fetch_childs_attrs -> id2childAttrs

# copy_object -> copy_stobj

# move_object -> copy_stobj

class StObj:
    
    def __init__(self):
        self.table = 'stobj'
        self.id = 'id'
        self.path = 'path'
        self.type = 'type'
        self.parent_id = 'parent_id'
        self.state = 'state'
        
        self.typeAt = 'account'
        self.typeCn = 'container'
        self.typeLk = 'link'
        self.typeDr = 'dir'
        self.typeFl = 'file'
        
def onepath2id(conn,path,parent_id):

    # fetch_one_path_id
    
    s = StObj()
    
    attrs = [s.id]
    table = s.table
    condition = {s.parent_id:parent_id,
                 s.path:path}
    
    data = conn.select(attrs,table,condition) 
    if data:
        return data[0][0]
     
    return -1

def account2id(conn,path):

    # fetch_account_id
    
    s = StObj()
    attrs = [s.id]
    table = s.table
    
    condition = {s.type:s.typeAt,
                 s.path:path}
    
    data = conn.select(attrs,table,condition)
    if data:
        return data[0][0]

    return -1

def fullPath2id(conn,path,parent=False):

    # fetch_path_id
    # if parent is True,then path will be insert to db though not exists 
    s = StObj()
    
    level = 0
    id = -1
    for ph in path.split('/'):
        if not ph:
            continue

        if 0 == level:
            id = account2id(conn,ph)
            level = level+1
            continue
        parent_id = id
        id = onepath2id(conn,ph,parent_id)
        if -1 == id:
            if parent:
                insert_stobj(conn,s.typeDr,ph,parent_id,'') 
                id = onepath2id(conn,ph,parent_id)
            else:
                break
        level = level + 1

    return id

def insert_stobj(conn,stobj_type,stobj_path,stobj_parent_id,stobj_state):
     
    s = StObj()
    keys = [s.type,s.path]
    vals = [stobj_type,stobj_path]
    
    if stobj_parent_id:
        keys.append(s.parent_id)
        vals.append(stobj_parent_id)
        
    if stobj_state:
        keys.append(s.state)
        vals.append(stobj_state)
        
    return conn.insert(keys,vals,s.table)
    
def delete_stobj(conn,id):

    s = StObj()    
    return conn.delete(s.table,{s.id:str(id)})
    
def insert_object(conn,stobj_type,stobj_path,abs_parent,stobj_state):

    parent_id = fullPath2id(conn,abs_parent,parent=True)
    if -1 == parent_id:
        return False,'fetch parent path id error'
    return insert_stobj(conn,stobj_type,stobj_path,parent_id,stobj_state)

def delete_child_stobj(conn,id):

    s = StObj()
    
    return conn.delete(s.table,{s.parent_id:id})

def id2attrs(conn,id):

    attrs = {}
    
    s = StObj()
    datas = conn.select(['*'],s.table,{s.id:str(id)})
    
    if datas:
        data = datas[0]
        attrs[s.id] = data[0]
        attrs[s.path] = data[1]
        attrs[s.type] = data[2]
        attrs[s.parent_id] = data[3]
        attrs[s.state] = data[4]
        return attrs
    return attrs

def fullPath2attrs(conn,fullPath):

    id = fullPath2id(conn,fullPath,parent=False) 
    attrs = id2attrs(conn,id)
    return attrs

def id2childAttrs(conn,parent_id):
    
    cldsattrs = []
    
    s = StObj()
    datas = conn.select(['*'],s.table,{s.parent_id:str(parent_id)})
        
    if datas:
        for data in datas:
            attrs = {}
            attrs[s.id] = data[0]
            attrs[s.path] = data[1]
            attrs[s.type] = data[2]
            attrs[s.parent_id] = data[3]
            attrs[s.state] = data[4]
            cldsattrs.append(attrs)
        return cldsattrs

    return cldsattrs

def id2treeAttrs(conn,parent_id):
    cldsattrs = []
    
    s = StObj()
    datas = conn.select(['*'],s.table,{s.parent_id:str(parent_id)})
        
    if datas:
        for data in datas:
            attrs = {}
            attrs[s.id] = data[0]
            attrs[s.path] = data[1]
            attrs[s.type] = data[2]
            attrs[s.parent_id] = data[3]
            attrs[s.state] = data[4]
            if 'dir' == attrs[s.type]:
                attrs['list'] = id2treeAttrs(conn, attrs[s.id])
            cldsattrs.append(attrs)
    return cldsattrs

def id2urlAttrs(id,db):
    
    s = StObj()
    
    path = ''
    attr = id2attrs(db,id)
    if not attr:
        return False,'object not found by id'
    path = attr.get(s.path)
    parent_id = attr.get(s.parent_id)
    type = attr.get(s.type)
    
    while parent_id and parent_id>-1:
        
        id = parent_id
        tmpattr = id2attrs(db,id)
        path = '/'.join([tmpattr[s.path],path])
        parent_id = tmpattr.get(s.parent_id)
        
    attr[s.path] = path
    return True,attr

def copy_stobj(conn,srcNewPath,dstNewPath):

    s = StObj()
    
    queueids = []
    attrs = fullPath2attrs(conn,fullPath = srcNewPath)      
    new_parent_id = fullPath2id(conn,'/'.join(dstNewPath.split('/')[:-1]),parent=True) 
    newPath = dstNewPath.split('/')[-1]
    attrs[s.parent_id] = new_parent_id
    attrs[s.path] = newPath

    queueids.append(attrs)
    while len(queueids) >0:
        attrs = queueids.pop(0)
        insert_stobj(conn,attrs[s.type],attrs[s.path],attrs[s.parent_id],attrs[s.state])
        new_parent_id = onepath2id(conn,attrs[s.path],attrs[s.parent_id])
        cldattrs = id2childAttrs(conn,attrs[s.id])
        for attrs in cldattrs:
            attrs[s.parent_id] = new_parent_id
        queueids.extend(cldattrs) 
    return True,''
    
def move_stobj(conn,srcNewPath,dstNewPath):

    id = fullPath2id(conn,srcNewPath)

    absDstNewPath = '/'.join(dstNewPath.split('/')[:-1])
    dstPh = dstNewPath.split('/')[-1]
    new_parent_id = fullPath2id(conn,absDstNewPath,parent=True)

    return update_parent(conn,id,new_parent_id,dstPh)

def update_stobj(db,id,newPid='',dstPath='',state=''):
    
    # sql = "update stobj set parent_id=%s,path='%s' where id=%s " % (str(new_parent_id),path,str(id))
    
    s = StObj()
    d = {}
    if newPid:
        d.update({s.parent_id:newPid})
    if dstPath:
        d.update({s.path:dstPath})
    if state:
        d.update({s.state:state})
        
    return db.update(d,s.table,{s.id:id})

def update_parent(db,id,new_parent_id,path):

    return update_stobj(db,id,newPid=new_parent_id,dstPath=path)

