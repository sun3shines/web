# -*- coding: utf-8 -*-

import subprocess

def get_hw_mem():
    local_mems = []
    hw = subprocess.Popen(['dmidecode'], 
                              stdout=subprocess.PIPE)

    host = subprocess.Popen(['grep','-A18', 'Memory Device$'],
                             stdin=hw.stdout,stdout=subprocess.PIPE)
    mems = host.stdout.read()
    mems = mems.split('Memory Device') 
    adds = []
    for mem in mems:
        if not mem:
            continue
        total_width = data_width = size = form_factor = speed = "NA"
        manufacturer = serial = asset_tag = part_number = "NA"
        for line in mem.split('\n'):
            line = line.strip()
            
            if line.startswith("Total Width"):
                total_width = line.split(":")[1].strip()
            elif line.startswith("Data Width"):
                data_width = line.split(":")[1].strip()
            elif line.startswith("Size"):
                size = line.split(":")[1].strip()
            elif line.startswith("Form Factor"):
                form_factor = line.split(":")[1].strip()
            elif line.startswith("Speed"):
                speed = line.split(":")[1].strip()
            elif line.startswith("Manufacturer"):
                manufacturer = line.split(":")[1].strip()
            elif line.startswith("Serial Number"):
                serial = line.split(":")[1].strip()
            elif line.startswith("Asset Tag"):
                asset_tag = line.split(":")[1].strip()
            elif line.startswith("Part Number"):
                part_number = line.split(":")[1].strip()
           
        if serial in adds:
            continue
        adds.append(serial) 
        local_mem = {'total_width':total_width,'data_width':data_width,'size':size,'form_factor':form_factor,
                     'speed':speed,'manufacturer':manufacturer,'serial':serial,'asset_tag':asset_tag,
                     'part_number':part_number}
        
        local_mems.append(local_mem)
    return local_mems

if __name__ == '__main__':
    print get_hw_mem()
