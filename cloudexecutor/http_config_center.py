# -*- coding: utf-8 -*-

import json
import socket
from cloudlib.common.bufferedhttp import jresponse
from cloudlib.utils.uuid import loadUuid

def centerPullExecutor(request):
    host_info = {'uuid':loadUuid(),
                 'name':socket.gethostname()}
    return jresponse('0',json.dumps(host_info),request,200)

def centerSetConfig(request):
    return jresponse('0','',request,200)

def centerGetConfig(request):
    return jresponse('0','',request,200)
