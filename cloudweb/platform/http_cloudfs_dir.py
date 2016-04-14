# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse

def cloudfsDirPut(req):
    return jresponse('0','',req,200)

def cloudfsDirDelete(req):
    return jresponse('0','',req,200)

def cloudfsDirReset(req):
    return jresponse('0','',req,200)

def cloudfsDirDeleteRecycle(req):
    return jresponse('0','',req,200)

def cloudfsDirMoveRecycle(req):
    return jresponse('0','',req,200)

def cloudfsDirMove(req):
    return jresponse('0','',req,200)

def cloudfsDirCopy(req):
    return jresponse('0','',req,200)

def cloudfsDirMetaGet(req):
    return jresponse('0','',req,200)

def cloudfsDirGet(req):
    return jresponse('0','',req,200)
