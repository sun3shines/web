# -*- coding: utf-8 -*-

from cloudexecutor.libconfig.libst import _stget,_stset
from cloudlib.globalx.config import EX_ACCOUNT_CONF_PATH,EX_CONTAINER_CONF_PATH,\
    EX_OBJECT_CONF_PATH,EX_PROXY_CONF_PATH
    
conf2st = {'storage_devices':[(EX_PROXY_CONF_PATH,'DEFAULT','devices'),(EX_ACCOUNT_CONF_PATH,'DEFAULT','devices'),
                              (EX_CONTAINER_CONF_PATH,'DEFAULT','devices'),(EX_OBJECT_CONF_PATH,'DEFAULT','devices')]}

def libSetStorage(attr):
    for key,val in attr.items():
        if key not in conf2st:
            continue
        for path,sec,option in conf2st.get(key):
            _stset(path, sec, option, val)
             
def libGetStorage():
    
    attr = {}
    for key in conf2st:
        val = ''
        for path,sec,option in conf2st.get(key):
            val = _stget(path, sec, option)
            attr.update({key:val})
            break
    return attr

if __name__ == '__main__':
#    print libGetStorage()
#    libSetStorage({'storage_devices':'/srv'})
#    print libGetStorage()

    libSetStorage({'storage_devices':'/mnt/cloudfs-object'})
    print libGetStorage()
