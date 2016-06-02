# -*- coding: utf-8 -*-

import re
import subprocess

from cloudmonitor.static.lshw import filter_hw,get_hw

def get_network_info(interface):
    output = subprocess.Popen(['ip', 'addr', 'show', 'dev', interface], stdout=subprocess.PIPE).communicate()[0].rsplit('\n')
    mtu = re.findall('mtu ([0-9]+) ', output[0])[0]
    link_ha = re.findall('link/(\w+) ([0-9a-fA-F:]+) ', output[1])[0]
    inet = {"addr": "NA", "mask": "NA"} 
    inet6 = {"addr": "NA", "mask": "NA"} 
    for line in output[2:]:   
        if not inet:
            tinet = re.findall('inet ([0-9\.]+)/([0-9]+) ', line)
            if tinet:
                inet = {"addr": tinet[0][0], "mask": tinet[0][1]}
                continue
        if not inet6:
            tinet6 = re.findall('inet6 ([0-9a-fA-F:]+)/([0-9]+) ', line)
            if (tinet6):
                inet6 = {"addr": tinet6[0][0], "mask": tinet6[0][1]}
        if inet and inet6:
            break  
    return {"mtu":int(mtu), "link": link_ha[0], "mac": link_ha[1], "inet": inet['addr'], 
            "inetmask":inet["mask"], "inet6add": inet6["addr"],"inet6mask":inet6["mask"],"is_primary":"NA"}

def get_hw_net(hw):
    local_nets = []
    # the disks
    nets = filter_hw(hw, "network")
    for net in nets:
        if net['id'].startswith('network'): 
            logname = "NA"
            if "logicalname" in net:
                if isinstance(net['logicalname'], list):
                    logname = net['logicalname'][0]
                else:
                    logname = net['logicalname']    
            else :
                continue
            description = "NA"
            if "description" in net: 
                description = net["description"]          
            product = "NA"
            if "product" in net: 
                product = net["product"]
            vendor = "NA"
            if "vendor" in net: 
                vendor = net["vendor"]          
            physid = "NA"
            if "physid" in net:
                physid = net["physid"] 
            businfo = "NA"
            if "businfo" in net:
                businfo = net["businfo"]        
            netversion = "NA"
            if "version" in net:
                netversion = net["version"]         
            serial = "NA"
            if "serial" in net:
                serial = net["serial"]        
            netsize = 0
            if "size" in net:    
                if net["units"] == "bit/s":
                    netsize = net["size"]
            netwidth = 0
            if "width" in net:
                if net["units"] == "bit/s":
                    netwidth = net["width"]
            netclock = 0
            if "clock" in net:
                if net["units"] == "bit/s":
                    netclock = net["clock"]
            netcapacity = 0
            if "capacity" in net:    
                if net["units"] == "bit/s":
                    netcapacity = net["capacity"]
                # other units ?                  
            d = {"description": description,
                 "product": product,
                 "vendor": vendor,
                 "physical_id": physid,
                 "logicalname": logname,
                 "bus_info":businfo,
                 "version": netversion,
                 "serial": serial,
                 "size": netsize,
                 "capacity": netcapacity,
                 "width":netwidth,
                 "clock":netclock
                 }
            d_info = get_network_info(logname)
            d.update(d_info)
            local_nets.append(d)
    return local_nets

if __name__ == '__main__':
    hw = get_hw()
    print get_hw_net(hw) 
