# -*- coding: utf-8 -*-

class Network:
    def __init__(self):
        self.table = 'stat_net'
        self.id = 'id'
        self.hid = 'host_id'
        self.timestamp = 'timestamp'
        self.bytes_sent_per_sec = 'bytes_sent_per_sec'
        self.bytes_recv_per_sec = 'bytes_recv_per_sec'
        self.packet_send_per_sec = 'packet_send_per_sec'
        self.packet_recv_per_sec = 'packet_recv_per_sec'
        self.seq = 'seq'
        
        
def insert_net(db,hid,timestamp,bytes_sent_per_sec,bytes_recv_per_sec,
               packet_send_per_sec,packet_recv_per_sec,seq):
    
    n = Network()
    keys = [n.hid,n.timestamp,n.bytes_sent_per_sec,n.bytes_recv_per_sec,
            n.packet_send_per_sec,n.packet_recv_per_sec,n.seq]
    vals = [hid,timestamp,bytes_sent_per_sec,bytes_recv_per_sec,
            packet_send_per_sec,packet_recv_per_sec,seq]
    return db.insert(keys,vals,n.table)

def update_net(db,nid,timestamp,bytes_sent_per_sec,bytes_recv_per_sec,
               packet_send_per_sec,packet_recv_per_sec,seq):
    n = Network()
    d = {}
    d.update({n.timestamp:timestamp,n.bytes_sent_per_sec:bytes_sent_per_sec,
              n.bytes_recv_per_sec:bytes_recv_per_sec,n.packet_send_per_sec:packet_send_per_sec,
              n.packet_recv_per_sec:packet_recv_per_sec,n.seq:seq})
    return db.update(d,n.table,{n.id:nid})

def fetch_net(db,hid):
    n = Network()
    attrs = [n.id,n.hid,n.timestamp,n.bytes_sent_per_sec,n.bytes_recv_per_sec,
             n.packet_send_per_sec,n.packet_recv_per_sec,n.seq]
    cond = {n.hid:hid}
    return db.select(attrs,n.table,cond)

def hid2attrs(db,hid):
    attrs = []
    n = Network()
    datas = fetch_net(db, hid)
    truncated =  datas
    for data in truncated:
        attr = {}
        attr[n.id] = data[0]
        attr[n.hid] = data[1]
        attr[n.timestamp] = data[2]
        attr[n.bytes_sent_per_sec] = data[3]
        attr[n.bytes_recv_per_sec] = data[4]
        attr[n.packet_send_per_sec] = data[5]
        attr[n.packet_recv_per_sec] = data[6]
        attr[n.seq] = data[7]
        attrs.append(attr)
    return attrs

