# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudlib.restful.cloudfs.lib_quota import libGetQuota,libSetQuota
from cloudweb.globalx.variable import GLOBAL_USER_TOKEN

def flaskQuotaGet(req,sdata):

    param = json.loads(req.body)
    atName = param.get('atName')

    usertoken = GLOBAL_USER_TOKEN.get_user_token(atName)
    resp = libGetQuota(atName, usertoken)
    
    return jresponse(resp['status'],resp['msg'],req,200)

def flaskQuotaSet(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    val = param.get('val')
    
    usertoken = GLOBAL_USER_TOKEN.get_user_token(atName)
    resp = libSetQuota(atName, usertoken, val)
    return jresponse(resp['status'],resp['msg'],req,200)
