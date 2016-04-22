# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.monitor.globalx import GlobalQueue

def processStatData(request):

    param = json.loads(request.body)
    hostUuid = param.get('hostUuid')
    typeClass = param.get('class')
    attr = param.get('attr')
    if not GlobalQueue.get(hostUuid):
        return jresponse('0','restart',request,200)
    
    GlobalQueue.get(hostUuid).get(typeClass).put(attr)
    # GlobalQueue.get(hostUuid).get('host').put(attr)
    return jresponse('0','',request,200)
