# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.platform.globalx.variable import GLOBAL_USER_TOKEN,GLOBAL_ADMIN_TOKENS
from cloudweb.platform.drive.utils import getAtNameByEmail

def cloudfsOauthRegister(req):
    
    param = json.loads(req.body)
    email = param.get('email')
    passwd = param.get('passwd')
    usertoken = param.get('usertoken')
    atName = getAtNameByEmail(email)
    GLOBAL_USER_TOKEN.put(atName, email, passwd, usertoken)
    
    return jresponse('0','',req,200)

def cloudfsOauthTokenValid(req):

    param = json.loads(req.body)
    admintoken = param.get('usertoken')
    if GLOBAL_ADMIN_TOKENS.has_item(admintoken):
        ecode = '0'
    else:
        ecode = '-1'
    return jresponse(0,ecode,req,200)

        
