# -*- coding: utf-8 -*-

from cloudlib.common.exceptions import LockTimeout, MessageTimeout
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.platform.flask_urls import flaskUrl2View

url2view = {}
url2view.update(flaskUrl2View())

def handlerequest(req,sdata):
    url = req.path
    if url not in url2view:
        return jresponse('-1','url error',req,404)
    return url2view[url](req,sdata)


