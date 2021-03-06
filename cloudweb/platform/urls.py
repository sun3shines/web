# -*- coding: utf-8 -*-

from cloudlib.common.bufferedhttp import jresponse
from cloudweb.platform.flask_urls import flaskUrl2View
from cloudweb.platform.cloudfs_urls import cloudfsUrl2View

url2view = {}
url2view.update(flaskUrl2View())
url2view.update(cloudfsUrl2View())

def handlerequest(req):

    url = req.path
    print url
    if url not in url2view:
        return jresponse('-1','url error',req,404)
    if url.startswith('/cloudfs'):
        return url2view[url](req)
    else: 
        return url2view[url](req)


