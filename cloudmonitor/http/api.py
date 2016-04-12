# -*- coding: utf-8 -*-

import json

from cloudmonitor.http.task import Task
from cloudlib.urls.monitor import urlStartUp,urlStatData
import cloudmonitor.http.mission as mission

class StartUp(Task):
    def __init__(self,param):
        self.param = param
    
    def getUrl(self):
        return urlStartUp
    
    def getBody(self):
        return json.dumps(self.param)
    
class StatData(Task):
    def __init__(self,data):
        self.data = data
    
    def getUrl(self):
        return urlStatData
    
    def getBody(self):
        return json.dumps(self.data)
    
def monitor_start(param):
    t = StartUp(param)
    mission.execute(t)
    print t.response
    return t.response

def monitor_stat(data):
    t = StatData(data)
    mission.execute(t)
    print t.response
    return t.response    
