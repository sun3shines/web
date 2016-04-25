# -*- coding: utf-8 -*-

from cloudexecutor.libconfig.libst import _stget,_stset
from cloudlib.globalx.config import EX_ACCOUNT_CONF_PATH,EX_CONTAINER_CONF_PATH,\
    EX_OBJECT_CONF_PATH,EX_PROXY_CONF_PATH
    
conf2st = {'concurrency_proxy':[(EX_PROXY_CONF_PATH,'DEFAULT','workers')],
           'concurrency_account':[(EX_ACCOUNT_CONF_PATH,'DEFAULT','workers')],
           'concurrency_container':[(EX_CONTAINER_CONF_PATH,'DEFAULT','workers')],
           'concurrency_object':[(EX_OBJECT_CONF_PATH,'DEFAULT','workers')]}

def libSetConCurrency(attr):
    for key,val in attr.items():
        if key not in conf2st:
            continue
        for path,sec,option in conf2st.get(key):
            _stset(path, sec, option, val)
             
def libGetConCurrency():
    
    attr = {}
    for key in conf2st:
        val = ''
        for path,sec,option in conf2st.get(key):
            val = _stget(path, sec, option)
            attr.update({key:val})
            break
    return attr

if __name__ == '__main__':
    
    #print libGetConCurrency()
    #libSetConCurrency({'concurrency_proxy':'2',
    #                   'concurrency_account':'3',
    #                   'concurrency_container':'4',
    #                   'concurrency_object':'5'})
    #print libGetConCurrency()
    libSetConCurrency({'concurrency_proxy':'0',
                       'concurrency_account':'0',
                       'concurrency_container':'0',
                       'concurrency_object':'0'})
    print libGetConCurrency()
    