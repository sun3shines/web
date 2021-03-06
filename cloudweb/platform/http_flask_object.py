# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudlib.restful.cloudfs.lib_file import libUploadFile,libDownloadFile,libDeleteFile
from cloudweb.platform.globalx.variable import GLOBAL_USER_TOKEN,GLOBAL_USER_DB
from cloudweb.dblib.db_flask_object import db_flask_object_disable,db_flask_object_enable
from cloudlib.common.common.swob import Response as HResponse
from cloudweb.platform.drive.consistency import flask_consistent
from cloudweb.db.table.lock.mysql import getlock

def flaskUploadObject(req):

    # 上传文件时，参数不使用request.body
    # 因此一致性无法保证了。所以不执行一致性同步，由登录保证
    param = req.GET
    atName = param.get('atName').encode('utf-8')
    objPath = param.get('objPath').encode('utf-8')
    
    usertoken = GLOBAL_USER_TOKEN.get_user_token(atName) or req.GET.get('x_admin_token')
    resp = libUploadFile(atName, usertoken, objPath, '', handle=req.environ['wsgi.input'], headers=req.headers)
    return jresponse(resp['status'],resp['msg'],req,200)

@flask_consistent
def flaskDownloadObject(req):

    param = json.loads(req.body)
    atName = param.get('atName').encode('utf-8')
    objPath = param.get('objPath').encode('utf-8')

    usertoken = GLOBAL_USER_TOKEN.get_user_token(atName) or req.GET.get('x_admin_token')
    app_iter = libDownloadFile(atName, usertoken, objPath)

    return HResponse(app_iter=app_iter,request=req,conditional_response=True)

@flask_consistent
def flaskDeleteObject(req):
    
    param = json.loads(req.body)
    atName = param.get('atName').encode('utf-8')
    objPath = param.get('objPath').encode('utf-8')
    
    usertoken = GLOBAL_USER_TOKEN.get_user_token(atName) or req.GET.get('x_admin_token')
    resp = libDeleteFile(atName, usertoken, objPath)
    
    return jresponse(resp['status'],resp['msg'],req,200)

@flask_consistent
def flaskEnableObject(req):
    
    param = json.loads(req.body)
    atName = param.get('atName').encode('utf-8')
    objPath = param.get('objPath').encode('utf-8')
    
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        newPath = '/'.join([atName,objPath])
        db_flask_object_enable(conn,newPath)
    return jresponse('0',json.dumps({}),req,200)

@flask_consistent
def flaskDisableObject(req):
    
    param = json.loads(req.body)
    atName = param.get('atName').encode('utf-8')
    objPath = param.get('objPath').encode('utf-8')
    
    conn = GLOBAL_USER_DB.get(atName)
    
    newPath = '/'.join([atName,objPath])
    with getlock(conn) as mylock:
        db_flask_object_disable(conn,newPath)
    return jresponse('0',json.dumps({}),req,200)

