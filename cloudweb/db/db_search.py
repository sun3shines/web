# -*- coding: utf-8 -*-

from cloudweb.db.table.stobj import StObj,fullPath2attrs,id2childAttrs

def search_global_objects(conn,keyword):
    
    objects = []
    
    s = StObj()
    datas = conn.select(['*'],s.table,{}," where path like'%" + keyword + "%'" )
    if datas:
        for data in datas:
            attr = {}
            attr['id'] = data[0]
            attr['path'] = data[1]
            attr['type'] = data[2]
            attr['parent_id'] = data[3]
            attr['state'] = data[4]
            objects.append(attr)
        return objects

    return objects

def search_account_objects(conn,atName,keyWord):

    objects = []
    queueids = []
    attrs = fullPath2attrs(conn,fullPath = atName)
    queueids.append(attrs)

    while len(queueids) >0:
        attrs = queueids.pop(0)

        if attrs['path'].find(keyWord) != -1:
            objects.append(attrs)

        cldattrs = id2childAttrs(conn,attrs['id'])
        queueids.extend(cldattrs)
     
    return objects

