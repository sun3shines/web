# -*- coding: utf-8 -*-
import psutil
import time
import datetime

from cloudmonitor.globalx import PSUTIL_NET_INTERVAL

def net_iter():
    
    total_before = total_after = None
    while True:
        if total_after:
            total_before = total_after
        else:
            total_before = psutil.network_io_counters()
        time.sleep(PSUTIL_NET_INTERVAL)
        total_after = psutil.network_io_counters()
        bytes_sent = total_after.bytes_sent - total_before.bytes_sent
        bytes_recv = total_after.bytes_recv - total_before.bytes_recv
        packet_sent = total_after.packets_sent - total_before.packets_sent
        packet_recv = total_after.packets_recv - total_before.packets_recv
        bytes_sent_per_sec = bytes_sent/PSUTIL_NET_INTERVAL
        bytes_recv_per_sec = bytes_recv/PSUTIL_NET_INTERVAL
        packet_send_per_sec = packet_sent/PSUTIL_NET_INTERVAL
        packet_recv_per_sec = packet_recv/PSUTIL_NET_INTERVAL
        
        yield (bytes_sent_per_sec,bytes_recv_per_sec,
               packet_send_per_sec,packet_recv_per_sec)
        
def get_psutil_net(hostUuid):
    
    for bytes_sent_per_sec,bytes_recv_per_sec,packet_send_per_sec, packet_recv_per_sec in net_iter():
        
        yield {'hostUuid':hostUuid,
               'class':'statNet',
               'attr':{'timestamp':str(datetime.datetime.now()),
                       'bytes_sent_per_sec':bytes_sent_per_sec,
                       'bytes_recv_per_sec':bytes_recv_per_sec,
                       'packet_send_per_sec':packet_send_per_sec,
                       'packet_recv_per_sec':packet_recv_per_sec}}
        
