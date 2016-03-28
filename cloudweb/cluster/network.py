
# def getNetDevs():
import dbus
import isys

from cloudweb.cluster.exe import sysCmd 
from cloudweb.cluster.config import ipExprPtn,macExprPtn,maskExprPtn,devExprPtn,linkExprPtn
from cloudweb.cluster.reg import exprSearch,exprFindAll

def getActiveNetDevs():
    active_devs = set()

    bus = dbus.SystemBus()
    nm = bus.get_object(isys.NM_SERVICE, isys.NM_MANAGER_PATH)
    nm_props_iface = dbus.Interface(nm, isys.DBUS_PROPS_IFACE)

    active_connections = nm_props_iface.Get(isys.NM_MANAGER_IFACE, "ActiveConnections")

    for connection in active_connections:
        active_connection = bus.get_object(isys.NM_SERVICE, connection)
        active_connection_props_iface = dbus.Interface(active_connection, isys.DBUS_PROPS_IFACE)
        devices = active_connection_props_iface.Get(isys.NM_ACTIVE_CONNECTION_IFACE, 'Devices')

        for device_path in devices:
            device = bus.get_object(isys.NM_SERVICE, device_path)
            device_props_iface = dbus.Interface(device, isys.DBUS_PROPS_IFACE)

            interface_name = device_props_iface.Get(isys.NM_DEVICE_IFACE, 'Interface')
            active_devs.add(interface_name)

    ret = list(active_devs)
    ret.sort()
    return ret

def getHostIPv6s():

    NetDevInfos = {}
    for dev in getActiveNetDevs():
        addrs = isys.getIPAddresses(dev,version=6)
        NetDevInfos[str(dev)] = addrs

    return NetDevInfos

def getHostIPv4s():

    NetDevInfos = {}
    for dev in getActiveNetDevs():
        addrs = isys.getIPAddresses(dev, version=4) 
        NetDevInfos[str(dev)] = addrs
       
    return NetDevInfos

def ifconfigCmd():
    argList = ['ifconfig','-a']
    outStr,errStr = sysCmd(argList)
    return outStr,errStr

def ethtoolCmd(netDev):
    argList = ['ethtool',netDev]
    outStr,errStr = sysCmd(argList)
    return outStr,errStr

def getNetInfoByCmd():

    outStr,errStr = ifconfigCmd()
    if errStr:
        return False,'configFailedMsg'
    for devStr in outStr.split('\n\n'):
        if not devStr.strip():
            continue
        devMatch = exprSearch(devExprPtn,devStr)
        print devMatch.group(1)
        devName = devMatch.group(1)
        ipMatch = exprSearch(ipExprPtn,devStr) 
        if ipMatch:
            print ipMatch.group(1)
        macMatch = exprSearch(macExprPtn,devStr)
        if macMatch:
            print macMatch.group(1)
        maskMatch = exprSearch(maskExprPtn,devStr)
        if maskMatch:
            print maskMatch.group(1)

        ethOut,ethErr = ethtoolCmd(devName)
        if ethErr:
            continue
        linkMatch = exprSearch(linkExprPtn,ethOut)
        if linkMatch:
            print linkMatch.group(1) 

if __name__ == '__main__':

#    print getActiveNetDevs()
#    print getHostIPv4s()
    getNetInfoByCmd() 
