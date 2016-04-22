# -*- coding: utf-8 -*-

import cloudlib.restful.config.http.mission as mission
from cloudlib.restful.config.http.config_task import ConfExecutorPull,ConfConfigGet,ConfConfigSet

    
def libPullExecutor(http_host,http_port):

    t = ConfExecutorPull()
    t = mission.execute(http_host, http_port, t)
    return t.response
