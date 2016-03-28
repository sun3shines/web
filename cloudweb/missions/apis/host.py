# -*- coding: utf-8 -*-

import cloudweb.missions.mission as mission
from cloudweb.missions.tasks.host import *

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