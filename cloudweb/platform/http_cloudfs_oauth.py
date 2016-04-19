# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.globalx.variable import GLOBAL_USER_TOKEN
from cloudweb.drive.utils import getAtNameByEmail

def cloudfsOauthRegister(req):
    
    param = json.loads(req.body)
    email = param.get('email')
    passwd = param.get('passwd')
    usertoken = param.get('usertoken')
    atName = getAtNameByEmail(email)
    GLOBAL_USER_TOKEN.put(atName, email, passwd, usertoken)
    
    return jresponse('0','',req,200)
