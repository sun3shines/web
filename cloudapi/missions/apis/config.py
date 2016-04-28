# -*- coding: utf-8 -*-

import cloudapi.missions.mission as mission
from cloudapi.missions.tasks.config import ExecutorAdd,ExecutorDel,ExecutorList,\
    ConfigGet,ConfigSet
    
def add_config_executor(atName,hostip):
    '''
    功能：添加需要配置节点
    输入：用户名，节点ip (测试cloudfs节点ip为192.168.36.201)
    输出：
    ''' 
    t = ExecutorAdd(atName,hostip)
    mission.execute(t)
    print t.response
    return t.response

def del_config_executor(atName,hostUuid):
    '''
    功能：删除配置节点
    输入：用户名，节点uuid
    输出：
    '''
    t = ExecutorDel(atName,hostUuid)
    mission.execute(t)
    print t.response
    return t.response

def get_config_executor_list(atName):
    '''
    功能：获取配置节点列表
    输入：用户名
    输出：节点主机名，节点uuid，节点ip，节点状态
    '''
    t = ExecutorList(atName)
    mission.execute(t)
    print t.response
    return t.response

def get_config(atName,hostUuid):
    '''
    功能：获取配置节点选项
    输入：用户名，主机uuid
    输出：
    {"cache": {"cache_memcache_host": "127.0.0.1", "cache_memcache_port": "11211"},
     "storage": {"storage_devices": "/mnt/cloudfs-object"},
     "concurrency": {"concurrency_container": "0", "concurrency_proxy": "0", 
                     "concurrency_account": "0", "concurrency_object": "0"},
     "auth": {"auth_oauth_host": "http://192.168.36.201", "auth_oauth_port": "8080"},
     "proxy": {"proxy_bind_port": "443"}}

    cache 缓存：cache_memcache_host memcache主机，cache_memcache_port memcache端口
    storage存储：storage_devices 存储挂载路径
    concurrency并发：concurrency_account 账户服务并发数，concurrency_container容器服务并发数，
                     concurrency_object对象服务并发数，concurrency_proxy代理服务并发数
    auth认证: auth_oauth_host认证主机地址，auth_oauth_port认证主机端口
    proxy代理：proxy_bind_port代理服务端口
    '''
    t = ConfigGet(atName,hostUuid)
    mission.execute(t)
    print t.response
    return t.response

def set_configs(atName,hostUuid,attrs):
    '''
    功能：配置节点选项
    输入：用户名，节点uuid，配置选项
    {'cache':{xxx},
     'storage':{xxx},
     ...
     ...
    }
    输出：
    '''
    t = ConfigSet(atName,hostUuid,attrs)
    mission.execute(t)
    print t.response
    return t.response

