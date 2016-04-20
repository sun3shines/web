# -*- coding: utf-8 -*-

import cloudapi.missions.mission as mission
from cloudapi.missions.tasks.host import ServiceStatus,WorkloadStatus,\
    AbnormalEvents,HostStatic

def get_service_status(atName,hostUuid):
    t = ServiceStatus(atName,hostUuid)
    mission.execute(t)
    print t.response
    return t.response

def get_workload_status(atName,hostUuid,className):
    
    t = WorkloadStatus(atName,hostUuid,className)
    mission.execute(t)
    print t.response
    return t.response

def get_host_static(atName):
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


