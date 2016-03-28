# -*- coding: utf-8 -*-

from cloudweb.db.table.stobj import StObj,fullPath2attrs,id2childAttrs

def search_global_objects(conn,keyword):
    
    objects = []
    
    s = StObj()
    datas = conn.select(['*'],s.table,{}," where path like'%" + keyword + "%'" )
    if datas:
        for data in datas:
            object = {}
            object['id'] = data[0]
            object['path'] = data[1]
            object['type'] = data[2]
            object['parent_id'] = data[3]
            object['state'] = data[4]
            objects.append(object)
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

