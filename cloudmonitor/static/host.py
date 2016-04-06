# -*- coding: utf-8 -*-

import subprocess
import socket

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
            'uuid':'hostxxx',
            'manufacturer':manufacturer,
            'product':product,
            'version':version,
            'serial':serial,
            'asset_tag':asset_tag,
            'available':'enable'}
        
if __name__ == '__main__':
    print get_hw_host()
 
