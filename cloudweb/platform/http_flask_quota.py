# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.events.restful.quota import getAtQuota,setAtQuota

def flaskQuotaGet(req,sdata):

    param = json.loads(req.body)
    atName = param.get('atName')

    ev = sdata.user.getUser(atName)
    resp = getAtQuota(ev)
    
    return jresponse(resp['status'],resp['msg'],req,200)

def flaskQuotaSet(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    val = param.get('val')
    
    ev = sdata.user.getUser(atName)
    resp = setAtQuota(ev, val)
    
    return jresponse(resp['status'],resp['msg'],req,200)
