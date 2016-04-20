# -*- coding: utf-8 -*-

from cloudweb.db.table.dynamic.stat_service import hid2attrs as service_hid2attrs

def query_service(db,hid):
    attrs = service_hid2attrs(db,hid) 
    sorted_attrs = sorted(attrs, key=lambda attr: attr.get('seq'),reverse=True) 
    service_list = []
    names = []
    for s in sorted_attrs:
        if s.get('name') not in names:
            names.append(s.get('name'))
            service_list.append(s)
        else:
            break
    return service_list
