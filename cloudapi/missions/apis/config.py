# -*- coding: utf-8 -*-

import cloudapi.missions.mission as mission
from cloudapi.missions.tasks.config import ExecutorAdd,ExecutorDel,ExecutorList,\
    ConfigGet,ConfigSet
    
def add_config_executor(atName,hostip):
    
    t = ExecutorAdd(atName,hostip)
    mission.execute(t)
    print t.response
    return t.response

def del_config_executor(atName,hostUuid):
    t = ExecutorDel(atName,hostUuid)
    mission.execute(t)
    print t.response
    return t.response

def get_config_executor_list(atName):
    t = ExecutorList(atName)
    mission.execute(t)
    print t.response
    return t.response

def get_config(atName,hostUuid):
    t = ConfigGet(atName,hostUuid)
    mission.execute(t)
    print t.response
    return t.response

def set_configs(atName,hostUuid,params):
    t = ConfigSet(atName,hostUuid,params)
    mission.execute(t)
    print t.response
    return t.response

