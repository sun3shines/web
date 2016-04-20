# -*- coding: utf-8 -*-

from cloudweb.db.table.dynamic.stat_cpu import hid2attrs as cpu_hid2attrs
from cloudweb.db.table.dynamic.stat_net import hid2attrs as net_hid2attrs
from cloudweb.db.table.dynamic.stat_disk import hid2attrs as disk_hid2attrs
from cloudweb.db.table.dynamic.stat_mem import getLatesMem as mem_hid2attrs
from cloudweb.db.table.dynamic.stat_storage import hid2attrs as storage_hid2attrs
from cloudweb.db.table.lock.mysql import getdb

def query_stat_cpu(db,hid):
    return cpu_hid2attrs(db, hid)

def query_stat_disk(db,hid):
    return disk_hid2attrs(db, hid)

def query_stat_net(db,hid):
    return net_hid2attrs(db, hid)

def query_stat_mem(db,hid):
    return mem_hid2attrs(db, hid)

def query_stat_storage(db,hid):
    attrs = storage_hid2attrs(db,hid) 
    sorted_attrs = sorted(attrs, key=lambda attr: attr.get('seq'),reverse=True) 
    storage_list = []
    uuids = []
    for s in sorted_attrs:
        if s.get('uuid') not in uuids:
            uuids.append(s.get('uuid'))
            storage_list.append(s)
        else:
            break
    return storage_list

if __name__ == '__main__':
    db = getdb()
    res = query_stat_storage(db,6)
    print res
