# -*- coding: utf-8 -*-

from cloudexecutor.libconfig.libst import _stget,_stset
from cloudlib.globalx.config import EX_ACCOUNT_CONF_PATH,EX_CONTAINER_CONF_PATH,\
    EX_OBJECT_CONF_PATH,EX_PROXY_CONF_PATH
    
conf2st = {'cache_memcache_host':[(EX_PROXY_CONF_PATH,'filter:cache','memcache_servers')],
           'cache_memcache_port':[(EX_PROXY_CONF_PATH,'filter:cache','memcache_servers')]}

def libSetCache(attr):
    
    for key,val in attr.items():
        if key not in conf2st:
            continue
        for path,sec,option in conf2st.get(key):
            old_vals = _stget(path, sec, option)
            old_host = old_vals.split(':')[0]
            old_port = old_vals.split(':')[1]
            if 'cache_memcache_host' == key:
                new_vals = ':'.join([val,old_port])
            else:
                new_vals = ':'.join([old_host,val])
            _stset(path, sec, option, new_vals)
             
def libGetCache():
    
    attr = {}
    for key in conf2st:
        val = ''
        for path,sec,option in conf2st.get(key):
            old_vals = _stget(path, sec, option)
            
            if 'cache_memcache_host' == key:
                val = old_vals.split(':')[0] 
            else:
                val = old_vals.split(':')[1] 
            attr.update({key:val})
            break
    return attr

if __name__ == '__main__':
    # print libGetCache()
#    libSetCache({'cache_memcache_host':'1.1.1.1'})
#    libSetCache({'cache_memcache_port':'11234'})
    libSetCache({'cache_memcache_host':'127.0.0.1',
                'cache_memcache_port':'11211'})
    print libGetCache()

