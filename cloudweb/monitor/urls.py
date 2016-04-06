# -*- coding: utf-8 -*-

from cloudcommon.common.exceptions import LockTimeout, MessageTimeout
from cloudcommon.common.bufferedhttp import jresponse
from cloudcommon.urls.monitor import *

from cloudweb.monitor.views.host import processStartUp
from cloudweb.monitor.views.stat import processStatData

url2view = {}

url2view.update({urlStartUp:processStartUp})

url2view.update({urlStatData:processStatData})

def handlerequest(req,sdata):
    url = req.path
    if url not in url2view:
        return jresponse('-1','url error',req,404)
    return url2view[url](req,sdata)
