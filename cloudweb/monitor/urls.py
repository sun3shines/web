# -*- coding: utf-8 -*-

from cloudlib.common.exceptions import LockTimeout, MessageTimeout
from cloudlib.common.bufferedhttp import jresponse
from cloudlib.urls.monitor import *

from cloudweb.monitor.views.host import processStartUp
from cloudweb.monitor.views.stat import processStatData

url2view = {}

url2view.update({urlStartUp:processStartUp})

url2view.update({urlStatData:processStatData})

def handlerequest(req):

    url = req.path
    if url not in url2view:
        return jresponse('-1','url error',req,404)
    return url2view[url](req)
