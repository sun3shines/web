# -*- coding: utf-8 -*-

import cloudlib.restful.config.http.mission as mission
from cloudlib.restful.config.http.config_task import ConfExecutorPull,ConfConfigGet,ConfConfigSet

    
def libPullExecutor(http_host,http_port):

    t = ConfExecutorPull()
    t = mission.execute(http_host, http_port, t)
    print t.response
    return t.response

def libSetExecutorConf(http_host,http_port,attrs):
    
    t = ConfConfigSet(attrs)
    t = mission.execute(http_host, http_port, t)
    print t.response
    return t.response
    
def libGetExecutorConf(http_host,http_port):
    
    t = ConfConfigGet()
    t = mission.execute(http_host, http_port, t)
    print t.response
    return t.response
    
if __name__ == '__main__':
    
    # libPullExecutor('192.168.36.3', 7015)
    attrs = {"cache": {"cache_memcache_host": "127.0.0.1", "cache_memcache_port": "11211"}, 
             "storage": {"storage_devices": "/mnt/cloudfs-object"}, 
             "concurrency": {"concurrency_container": "0", "concurrency_proxy": "0", "concurrency_account": "0", "concurrency_object": "0"}, 
             "auth": {"auth_oauth_host": "http://192.168.36.201", "auth_oauth_port": "8080"}, 
             "proxy": {"proxy_bind_port": "443"}}

#    attrs = {"cache": {"cache_memcache_host": "127.0.0.2", "cache_memcache_port": "11213"}, 
#             "storage": {"storage_devices": "/mnt/cloudfs-object11"}, 
#             "concurrency": {"concurrency_container": "6", "concurrency_proxy": "7", "concurrency_account": "8", "concurrency_object": "9"}, 
#             "auth": {"auth_oauth_host": "https://192.168.36.201", "auth_oauth_port": "8000"}, 
#             "proxy": {"proxy_bind_port": "423"}}
    libSetExecutorConf('192.168.36.201', 7015,attrs)
    libGetExecutorConf('192.168.36.201', 7015) 
