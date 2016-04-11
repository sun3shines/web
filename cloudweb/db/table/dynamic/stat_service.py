# -*- coding: utf-8 -*-

class Service:
    def __init__(self):
        self.table = 'stat_service'
        self.id = 'id'
        self.hid = 'host_id'
        self.timestamp = 'timestamp'
        self.name = 'name'
        self.cmdline = 'cmdline'
        self.active_status = 'active_status'
        self.open_files = 'open_files'
        self.net_connections = 'net_connections'
        self.thread_num = 'thread_num'
        self.cpu_utilization = 'cpu_utilization'
        self.mem_utilization = 'mem_utilization'
        self.avai = 'available'
        self.seq = 'seq'
        
        
def insert_service(db,hid,timestamp,name,cmdline,active_status,open_files,
                    net_connections,thread_num,cpu_utilizaiton,mem_utilization,avai,seq):
    
    s = Service()
    keys = [s.hid,s.timestamp,s.name,s.cmdline,s.active_status,s.open_files,
            s.net_connections,s.thread_num,s.cpu_utilization,s.mem_utilization,s.avai,s.seq]
    vals = [hid,timestamp,name,cmdline,active_status,open_files,
            net_connections,thread_num,cpu_utilizaiton,mem_utilization,avai,seq]
    return db.insert(keys,vals,s.table)

def update_service(db,sid,timestamp,name,cmdline,active_status,open_files,
                    net_connections,thread_num,cpu_utilizaiton,mem_utilization,avai,seq):
    s = Service()
    d = {}
    d.update({s.timestamp:timestamp,s.name:name,s.cmdline:cmdline,s.active_status:active_status,
              s.open_files:open_files,s.net_connections:net_connections,
              s.thread_num:thread_num,s.cpu_utilization:cpu_utilizaiton,
              s.mem_utilization:mem_utilization,s.avai:avai,s.seq:seq})
    return db.update(d,s.table,{s.id:sid})

def fetch_service(db,hid):
    s = Service()
    attrs = [s.id,s.hid,s.timestamp,s.name,s.cmdline,s.active_status,s.open_files,
             s.net_connections,s.thread_num,s.cpu_utilization,s.mem_utilization,s.avai,s.seq]
    cond = {s.hid:hid}
    return db.select(attrs,s.table,cond)

def hid2attrs(db,hid):
    attrs = []
    s = Service()
    datas = fetch_service(db, hid)
    truncated =  datas
    for data in truncated:
        attr = {}
        attr[s.id] = data[0]
        attr[s.hid] = data[1]
        attr[s.timestamp] = data[2]
        attr[s.name] = data[3]
        attr[s.cmdline] = data[4]
        attr[s.active_status] = data[5]
        attr[s.open_files] = data[6]
        attr[s.net_connections] = data[7]
        attr[s.thread_num] = data[8]
        attr[s.cpu_utilization] = data[9]
        attr[s.mem_utilization] = data[10]
        attr[s.avai] = data[11]
        attr[s.seq] = data[12]
        attrs.append(attr)
    return attrs

