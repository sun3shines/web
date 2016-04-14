# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse

def cloudfsAccountPut(req):
    
    return jresponse('0','',req,200)

def cloudfsAccountDelete(req):
    
    return jresponse('0','',req,200)

def cloudfsAccountExists(req):
    # 用户访问过于频繁，不实现    
    return jresponse('0','',req,200)

def cloudfsAccountGet(req):
    
    return jresponse('0','',req,200)

def cloudfsAccountPost(req):
    
    return jresponse('0','',req,200)

def cloudfsAccountHead(req):
    
    return jresponse('0','',req,200)


def cloudfsAccountMeta(req):
    
    return jresponse('0','',req,200)
