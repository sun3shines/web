# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudlib.restful.cloudfs.lib_quota import libGetQuota,libSetQuota
from cloudweb.platform.globalx.variable import GLOBAL_USER_TOKEN
from cloudweb.platform.drive.consistency import flask_consistent

@flask_consistent
def flaskQuotaGet(req):

    param = json.loads(req.body)
    atName = param.get('atName').encode('utf-8')

    usertoken = GLOBAL_USER_TOKEN.get_user_token(atName) or req.GET.get('x_admin_token')
    resp = libGetQuota(atName, usertoken)
    
    return jresponse(resp['status'],resp['msg'],req,200)

@flask_consistent
def flaskQuotaSet(req):
    
    param = json.loads(req.body)
    atName = param.get('atName').encode('utf-8')
    val = param.get('val')
    
    usertoken = GLOBAL_USER_TOKEN.get_user_token(atName) or req.GET.get('x_admin_token')
    resp = libSetQuota(atName, usertoken, val)
    return jresponse(resp['status'],resp['msg'],req,200)
