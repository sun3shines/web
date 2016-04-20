# -*- coding: utf-8 -*-

import cloudapi.missions.mission as mission
from cloudapi.missions.tasks.host import ServiceStatus,WorkloadStatus,\
    AbnormalEvents,HostStatic

def get_service_status(atName,hostUuid):
    '''
    功能：获取主机服务状态
    输入：用户名，主机uuid（通过get_host_static获取）
    输出：主机服务状态
    '''    
    t = ServiceStatus(atName,hostUuid)
    mission.execute(t)
    print t.response
    return t.response

def get_workload_status(atName,hostUuid,className):
   
    '''
    功能：获取主机运行负载信息
    输入：用户名，主机uuid，信息类型（cpu,mem,disk,net,storage）
    输出：主机负载类型数据，其中
    cpu：获取1000条主机运行数据
    mem：获取最新内存信息
    disk：获取1000条运行数据
    net：获取1000条运行数据
    storage：获取最新存储状态
    '''
 
    t = WorkloadStatus(atName,hostUuid,className)
    mission.execute(t)
    print t.response
    return t.response

def get_host_static(atName):
    '''
    功能：获取所有监控主机硬件配置信息
    输入：用户名
    输出：主机硬件配置数据，其中
    {'hostUuidA':{'cpu':{},'mem':{},'disk':{},'net':{},'host':{}},
     'hostUuidB':{'cpu':{},'mem':{},'disk':{},'net':{},'host':{}}} 
    host:主板信息
    cpu：cpu信息
    mem：内存信息
    disk：硬盘信息
    net：网卡数据
    '''

    t = HostStatic(atName)
    mission.execute(t)
    print t.response
    return t.response

def get_abnormal_events(atName):
    t = AbnormalEvents(atName)
    mission.execute(t)
    print t.response
    return t.response

if __name__ == '__main__':
#    get_service_status()
    pass


