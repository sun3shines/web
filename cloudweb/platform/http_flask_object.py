# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudlib.restful.cloudfs.lib_file import libUploadFile,libDownloadFile,libDeleteFile
from cloudweb.globalx.variable import GLOBAL_USER_TOKEN,GLOBAL_USER_DB
from cloudweb.dblib.db_flask_object import db_flask_object_disable,db_flask_object_enable
from cloudlib.common.common.swob import Response as HResponse

def flaskUploadObject(req,sdata):
    
    param = req.headers
    atName = param.pop('Atname')
    objPath = param.pop('Objpath')
    usertoken = GLOBAL_USER_TOKEN.get_user_token(atName)
    resp = libUploadFile(atName, usertoken, objPath, '', handle=req.environ['wsgi.input'], headers=param)
    return jresponse(resp['status'],resp['msg'],req,200)

def flaskDownloadObject(req,sdata):

    param = json.loads(req.body)
    atName = param.get('atName')
    objPath = param.get('objPath')

    usertoken = GLOBAL_USER_TOKEN.get_user_token(atName)
    app_iter = libDownloadFile(atName, usertoken, objPath)

    return HResponse(app_iter=app_iter,request=req,conditional_response=True)

def flaskDeleteObject(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    objPath = param.get('objPath')
    
    usertoken = GLOBAL_USER_TOKEN.get_user_token(atName)
    resp = libDeleteFile(atName, usertoken, objPath)
    
    return jresponse(resp['status'],resp['msg'],req,200)

def flaskEnableObject(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    objPath = param.get('objPath')
    
    conn = GLOBAL_USER_DB.get(atName)
    
    newPath = '/'.join([atName,objPath])
    db_flask_object_enable(conn,newPath)
    return jresponse('0',json.dumps({}),req,200)

def flaskDisableObject(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    objPath = param.get('objPath')
    
    conn = GLOBAL_USER_DB.get(atName)
    
    newPath = '/'.join([atName,objPath])
    db_flask_object_disable(conn,newPath)
    return jresponse('0',json.dumps({}),req,200)

