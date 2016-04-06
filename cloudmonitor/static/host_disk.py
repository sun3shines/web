# -*- coding: utf-8 -*-

from cloudmonitor.static.lshw import filter_hw,get_hw

def get_hw_disk(hw):  
    local_disks = [] 
    # the disks
    disks = filter_hw(hw, "disk")
    for disk in disks:
        if disk['id'].startswith('disk'): 
            logname = "NA"
            if "logicalname" in disk:
                if isinstance(disk['logicalname'], list):
                    logname = disk['logicalname'][0]
                else:
                    logname = disk['logicalname']
            else :
                continue
            description = "NA"
            if "description" in disk: 
                description = disk["description"]          
            product = "NA"
            if "product" in disk: 
                product = disk["product"]
            vendor = "NA"
            if "vendor" in disk: 
                vendor = disk["vendor"]          
            physid = "NA"
            if "physid" in disk:
                physid = disk["physid"]         
            diskversion = "NA"
            if "version" in disk:
                diskversion = disk["version"]         
            serial = "NA"
            if "serial" in disk:
                serial = disk["serial"]        
            disksize = 0
            if "size" in disk:    
                if disk["units"] == "bytes":
                    disksize = disk["size"]
            businfo = "NA"
            if "businfo" in disk:
                businfo = disk["businfo"]     
            # other units ?                  
            d = {"description": description,
                 "product": product,
                 "vendor": vendor,
                 "physical_id": physid,
                 "logicalname": logname,
                 "version": diskversion,
                 "serial": serial,
                 "size": disksize,
                 "bus_info":businfo
                 }
            local_disks.append(d)
    return local_disks

if __name__ == '__main__':
    hw = get_hw()
    print get_hw_disk(hw) 
    