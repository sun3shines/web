# -*- coding: utf-8 -*-

import cloudapi.missions.mission as mission
from cloudapi.missions.tasks.host import ServiceStatus,WorkloadStatus,\
    AbnormalEvents

def get_service_status(atName):
    t = ServiceStatus(atName)
    mission.execute(t)
    print t.response
    return t.response

def get_workload_status(atName):
    t = WorkloadStatus(atName)
    mission.execute(t)
    print t.response
    return t.response

def get_abnormal_events(atName):
    t = AbnormalEvents(atName)
    mission.execute(t)
    print t.response
    return t.response