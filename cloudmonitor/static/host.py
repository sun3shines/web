# -*- coding: utf-8 -*-

import subprocess
import socket
import time
from cloudmonitor.globalx import MONITOR_CONNECT_INTERVAL

from cloudlib.utils.uuid import loadUuid

from cloudmonitor.static.lshw import get_hw
from cloudmonitor.static.host_cpu import get_hw_cpu
from cloudmonitor.static.host_disk import get_hw_disk
from cloudmonitor.static.host_mem import get_hw_mem
from cloudmonitor.static.host_net import get_hw_net

from cloudmonitor.http.api import monitor_start

def get_hw_host():
    hw = subprocess.Popen(['dmidecode'], 
                              stdout=subprocess.PIPE)

    host = subprocess.Popen(['grep','-A13', 'Base Board Information$'],
                             stdin=hw.stdout,stdout=subprocess.PIPE) 
    output = host.stdout.readlines()
    product = manufacturer = version = serial = asset_tag = "NA"
    
    for line in output:
        line = line.strip()
        if line.startswith("Manufacturer"):
            manufacturer = line.split(":")[1].strip()
        elif line.startswith("Product Name"):
            product = line.split(":")[1].strip()
        elif line.startswith("Version"):
            version = line.split(":")[1].strip()
        elif line.startswith("Serial Number"):
            serial = line.split(":")[1].strip()
        elif line.startswith("Asset Tag"):
            asset_tag = line.split(":")[1].strip()
            
    return {'name':socket.gethostname(),
            'uuid':loadUuid(),
            'manufacturer':manufacturer,
            'product':product,
            'version':version,
            'serial':serial,
            'asset_tag':asset_tag,
            'available':'enable'}
        
def get_host_static():
    hwhost = get_hw_host()
    hw = get_hw()
    return {'hostUuid':hwhost.get('uuid'),'hostClass':hwhost,'cpuClass':get_hw_cpu(hw),
            'diskClass':get_hw_disk(hw),'memClass':get_hw_mem(),'netClass':get_hw_net(hw)}

def start():
    hostUuid = ''
    while True:
        host_hw = get_host_static()
        hostUuid = host_hw.get('hostUuid')
        resp = monitor_start(host_hw)
        if 'ready' == resp.get('msg'):
            break
        time.sleep(MONITOR_CONNECT_INTERVAL)
        
    return hostUuid

    
if __name__ == '__main__':
#    print get_hw_host()
    print get_host_static()
 
