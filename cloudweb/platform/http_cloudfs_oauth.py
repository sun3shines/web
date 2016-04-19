# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse

def cloudfsOauthRegister(req):
    
    param = json.loads(req.body)
    email = param.get('email')
    passwd = param.get('passwd')
    usertoken = param.get('usertoken')
    
    
    return jresponse('0','',req,200)
