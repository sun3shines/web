# -*- coding: utf-8 -*-

from cloudmonitor.static.lshw import filter_hw,get_hw

def get_hw_cpu(hw):
    local_cpus = []
    # the cpus
    cpus = filter_hw(hw, "processor")
    for cpu in cpus:
        if cpu['id'].startswith('cpu'): 
            description = "NA"
            if "description" in cpu: 
                description = cpu["description"]          
            product = "NA"
            if "product" in cpu: 
                product = cpu["product"]
            vendor = "NA"
            if "vendor" in cpu: 
                vendor = cpu["vendor"]          
            physid = "NA"
            if "physid" in cpu:
                physid = cpu["physid"]         
            cpuversion = "NA"
            if "version" in cpu:
                cpuversion = cpu["version"]          
            size = 0
            if "size" in cpu:    
                if cpu["units"] == "Hz":
                    size = cpu["size"]
            capacity = 0
            if "capacity" in cpu:    
                if cpu["units"] == "Hz":
                    capacity = cpu["capacity"]
            cpuwidth = 0
            if "width" in cpu:    
                cpuwidth = cpu["width"]
            businfo = "NA"
            if "businfo" in cpu:
                businfo = cpu["businfo"]     
            cpuclock = 0
            if "clock" in cpu:
                if cpu["units"] == "bit/s":
                    cpuclock = cpu["clock"]   
            cores = 0
            enabledcores = 0
            threads = 0
            if "configuration" in cpu:   
                config = cpu["configuration"]
                if "cores" in config:
                    cores = int(config["cores"])
                if "enabledcores" in config:
                    enabledcores = int(config["enabledcores"])
                if "threads" in config:
                    threads = int(config["threads"])

            c = {"description": description,
                 "product": product,
                 "vendor": vendor,
                 "physical_id": physid,
                 "bus_info":businfo,
                 "version": cpuversion,
                 "capacity": capacity,
                 "size": size, # frequency
                 "width": cpuwidth,
                 "clock":cpuclock,
                 "cores": cores,
                 "enabledcores": enabledcores,
                 "threads": threads,
                 }
            local_cpus.append(c)
            break
    return local_cpus

if __name__ == '__main__':
    hw = get_hw()
    print get_hw_cpu(hw)[0] 
    
