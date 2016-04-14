# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse

def cloudfsAccountValid(req):
    return jresponse('0','',req,200)

def cloudfsObjectValid(req):
    return jresponse('0','',req,200)