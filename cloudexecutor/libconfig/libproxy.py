# -*- coding: utf-8 -*-

from cloudexecutor.libconfig.libst import _stget,_stset
from cloudlib.globalx.config import EX_ACCOUNT_CONF_PATH,EX_CONTAINER_CONF_PATH,\
    EX_OBJECT_CONF_PATH,EX_PROXY_CONF_PATH

conf2st = {'proxy_bind_port':[(EX_PROXY_CONF_PATH,'DEFAULT','bind_port')]}

def libSetProxy(attr):
    for key,val in attr.items():
        if key not in conf2st:
            continue
        for path,sec,option in conf2st.get(key):
            _stset(path, sec, option, val)
             
def libGetProxy():
    
    attr = {}
    for key in conf2st:
        val = ''
        for path,sec,option in conf2st.get(key):
            val = _stget(path, sec, option)
            attr.update({key:val})
            break
    return attr

if __name__ == '__main__':
    print libGetProxy()
    libSetProxy({'proxy_bind_port':'556'})
    print libGetProxy()
    
