# -*- coding: utf-8 -*-
from cloudweb.db.table.static.host import queryattrs as host_queryattrs
from cloudweb.db.table.static.host import Host
from cloudweb.db.table.static.host_cpu import hid2attrs as cpu_hid2attrs
from cloudweb.db.table.static.host_mem import hid2attrs as mem_hid2attrs
from cloudweb.db.table.static.host_disk import hid2attrs as disk_hid2attrs
from cloudweb.db.table.static.host_net import hid2attrs as net_hid2attrs
from cloudweb.db.table.lock.mysql import getdb

def query_host_cpu(db,hid):
    return cpu_hid2attrs(db, hid)

def query_host_mem(db,hid):
    return mem_hid2attrs(db, hid)

def query_host_disk(db,hid):
    return disk_hid2attrs(db, hid)

def query_host_net(db,hid):
    return net_hid2attrs(db, hid)

def query_hosts(db):
    
    ht = Host()
    staticAttrs = {}
    hostAttrs = host_queryattrs(db)
    
    for attr in hostAttrs:
        staticAttrs.update({attr.pop(ht.uuid):{'host':attr}})
    return staticAttrs

def query_host_static(hostUuid):
    pass

def query_all_static(db):
    
    ht = Host()
    
    staticAttrs = query_hosts(db)
    
    for _,staticAttr in staticAttrs.items():
        host_id = staticAttr.get('host').get(ht.id)
        staticAttr.update({'cpu':query_host_cpu(db,host_id)})
        staticAttr.update({'mem':query_host_mem(db,host_id)})
        staticAttr.update({'disk':query_host_disk(db,host_id)})
        staticAttr.update({'net':query_host_net(db,host_id)})
    return staticAttrs

if __name__ == '__main__':
    import pdb;pdb.set_trace()
    conn = getdb()
    print query_all_static(conn)
    
