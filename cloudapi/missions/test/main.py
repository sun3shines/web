# -*- coding: utf-8 -*-

from cloudapi.missions.apis.fs import list_account,list_container,list_dir
from cloudapi.missions.apis.object import disable_object,enable_object,delete_object,\
    download_object,upload_object
from cloudapi.missions.apis.quota import get_account_quota,set_account_quota
from cloudapi.missions.apis.record import get_account_records,get_object_records
from cloudapi.missions.apis.search import data_global_find,data_user_find,data_md5_find,\
    get_object_details
from cloudapi.missions.apis.user import user_login,get_accounts,disable_account,\
    enable_account,delete_account
    
from cloudapi.missions.apis.host import get_host_static,get_service_status,get_workload_status
from cloudapi.missions.apis.config import add_config_executor,del_config_executor,get_config_executor_list,\
    get_config,set_configs
    
def fs_test(atName):
    list_account(atName)
    list_container(atName,'/normal')
    list_dir(atName,'/normal/dir')
    
def object_test(atName):
    
    upload_object(atName,'/normal/中国.txt','/root/install.log')
#    app_iter = download_object(atName,'/normal/test.txt')
#    for data in app_iter:
#        print data
#    disable_object(atName,'/normal/test.txt')
#    enable_object(atName,'/normal/test.txt')   
#    delete_object(atName,'/normal/中国.txt')

def quota_test(atName):

    get_account_quota(atName)
    set_account_quota(atName,str(1024*1024*1024))
    get_account_quota(atName)

def record_test(atName):

    get_account_records(atName)
    get_object_records(atName,'/normal/dir')

def search_test(atName):
#    data_user_find(atName,'normal')    
#    get_object_details(atName,'1340')
#    data_user_find(atName,'zhu__feng')
#    get_object_details(atName,'1339')
    data_user_find(atName,'中国')
#    get_object_details(atName,'1350')
def user_test(atName):
    
    disable_account(atName,atName) 
    enable_account(atName,atName)
    get_accounts(atName)
    delete_account(atName,atName)

def host_test(atName,hostUuid):
    get_host_static(atName)
    get_service_status(atName, hostUuid)
    get_workload_status(atName, hostUuid, 'cpu')
    get_workload_status(atName, hostUuid, 'mem')
    get_workload_status(atName, hostUuid, 'disk')
    get_workload_status(atName, hostUuid, 'net')
    get_workload_status(atName, hostUuid, 'storage')
    
def config_test(atName):
    pass
    add_config_executor(atName, '192.168.36.201')
#    get_config_executor_list(atName)
#    del_config_executor(atName,'fdxv5ohb-h07pox-smah')
    get_config_executor_list(atName)
#    attrs = {"cache": {"cache_memcache_host": "127.0.0.1", "cache_memcache_port": "11211"},
#             "storage": {"storage_devices": "/mnt/cloudfs-object"},
#             "concurrency": {"concurrency_container": "0", "concurrency_proxy": "0", "concurrency_account": "0", "concurrency_object": "0"},
#             "auth": {"auth_oauth_host": "http://192.168.36.201", "auth_oauth_port": "8080"},
#             "proxy": {"proxy_bind_port": "443"}}

#    attrs = {"cache": {"cache_memcache_host": "127.0.0.2", "cache_memcache_port": "11211"},
#             "storage": {"storage_devices": "/mnt/cloudfs-objectcc"},
#             "concurrency": {"concurrency_container": "3", "concurrency_proxy": "3", "concurrency_account": "3", "concurrency_object": "3"},
#             "auth": {"auth_oauth_host": "http://192.168.36.201", "auth_oauth_port": "800"},
#             "proxy": {"proxy_bind_port": "442"}}

#    set_configs(atName, 'fdxv5ohb-h07pox-smah', attrs)
#    get_config(atName, 'fdxv5ohb-h07pox-smah')    

if __name__ == '__main__': 

    email = 'zhu__feng001@163com'
    passwd = '123456'
    atName = 'AUTH_zhu__feng001163com'
#    email = 'testadministrator@163com'
#    passwd = '123456'
#    atName = 'AUTH_' + email.replace('@','').replace('.','')

    user_login(email,passwd)
    
#    fs_test(atName)
    object_test(atName)    
#    quota_test(atName)
#    record_test(atName)
    search_test(atName)
    
#    user_test(atName)
#    config_test(atName)
#    hostUuid = 'mIYuQsiH-1NmLgn-ny3t'
#    host_test(atName, hostUuid)
    
    
