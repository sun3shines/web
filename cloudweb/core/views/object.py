# -*- coding: utf-8 -*-

import json
from cloudcommon.common.bufferedhttp import jresponse
from cloudweb.events.restful.object import uploadFile,downloadFile,deleteFile
from cloudweb.db.object import enableOt,disableOt
from cloudcommon.common.common.swob import Response as HResponse

def uploadObject(req,sdata):
    
    param = req.headers
    atName = param.pop('Atname')
    objPath = param.pop('Objpath')
    
    ev = sdata.user.getUser(atName)
    resp = uploadFile(ev,objPath,'',handle=req.environ['wsgi.input'],headers=param)
    return jresponse(resp['status'],resp['msg'],req,200)

def downloadObject(req,sdata):

    param = json.loads(req.body)
    atName = param.get('atName')
    objPath = param.get('objPath')

    ev = sdata.user.getUser(atName)
    app_iter = downloadFile(ev,objPath)

    return HResponse(app_iter=app_iter,request=req,conditional_response=True)

def deleteObject(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    objPath = param.get('objPath')
    
    ev = sdata.user.getUser(atName)
    resp = deleteFile(ev,objPath)
    return jresponse(resp['status'],resp['msg'],req,200)

def enableObject(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    objPath = param.get('objPath')
    ev = sdata.user.getUser(atName)
    
    newPath = '/'.join([atName,objPath])
    enableOt(ev.db,newPath)
    return jresponse('0',json.dumps({}),req,200)

def disableObject(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    objPath = param.get('objPath')
    ev = sdata.user.getUser(atName)
    
    newPath = '/'.join([atName,objPath])
    disableOt(ev.db,newPath)
    return jresponse('0',json.dumps({}),req,200)
