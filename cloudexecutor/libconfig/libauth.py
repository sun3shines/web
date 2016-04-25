# -*- coding: utf-8 -*-

from cloudexecutor.libconfig.libst import _stget,_stset
from cloudlib.globalx.config import EX_ACCOUNT_CONF_PATH,EX_CONTAINER_CONF_PATH,\
    EX_OBJECT_CONF_PATH,EX_PROXY_CONF_PATH,EX_OPTION_OAUTH_HOST,EX_OPTION_OAUTH_PORT
    
conf2st = {EX_OPTION_OAUTH_HOST:[(EX_PROXY_CONF_PATH,'filter:oauth','oauth_host')],
           EX_OPTION_OAUTH_PORT:[(EX_PROXY_CONF_PATH,'filter:oauth','oauth_port')]}

def libSetAuth(attr):
    for key,val in attr.items():
        if key not in conf2st:
            continue
        for path,sec,option in conf2st.get(key):
            _stset(path, sec, option, val)
             
def libGetAuth():
    
    attr = {}
    for key in conf2st:
        val = ''
        for path,sec,option in conf2st.get(key):
            val = _stget(path, sec, option)
            attr.update({key:val})
            break
    return attr

if __name__ == '__main__': 
    # print libGetAuth()
    attr = {'auth_oauth_host':'https://192.168.36.201'}
    libSetAuth(attr)
