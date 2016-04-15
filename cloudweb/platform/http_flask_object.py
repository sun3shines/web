# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.events.restful.object import uploadFile,downloadFile,deleteFile
from cloudweb.dblib.db_flask_object import db_flask_object_disable,db_flask_object_enable
from cloudlib.common.common.swob import Response as HResponse

def flaskUploadObject(req,sdata):
    
    param = req.headers
    atName = param.pop('Atname')
    objPath = param.pop('Objpath')
    
    ev = sdata.user.getUser(atName)
    resp = uploadFile(ev,objPath,'',handle=req.environ['wsgi.input'],headers=param)
    return jresponse(resp['status'],resp['msg'],req,200)

def flaskDownloadObject(req,sdata):

    param = json.loads(req.body)
    atName = param.get('atName')
    objPath = param.get('objPath')

    ev = sdata.user.getUser(atName)
    app_iter = downloadFile(ev,objPath)

    return HResponse(app_iter=app_iter,request=req,conditional_response=True)

def flaskDeleteObject(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    objPath = param.get('objPath')
    
    ev = sdata.user.getUser(atName)
    resp = deleteFile(ev,objPath)
    return jresponse(resp['status'],resp['msg'],req,200)

def flaskEnableObject(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    objPath = param.get('objPath')
    ev = sdata.user.getUser(atName)
    
    newPath = '/'.join([atName,objPath])
    db_flask_object_enable(ev.db,newPath)
    return jresponse('0',json.dumps({}),req,200)

def flaskDisableObject(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    objPath = param.get('objPath')
    ev = sdata.user.getUser(atName)
    
    newPath = '/'.join([atName,objPath])
    db_flask_object_disable(ev.db,newPath)
    return jresponse('0',json.dumps({}),req,200)
