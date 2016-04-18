
# -*- coding: utf-8 -*-

import json
from cloudlib.restful.cloudfs.http.mission import TestMission
from cloudlib.restful.cloudfs.http.advanced_task import FileUpload,FileDownload
from cloudlib.restful.cloudfs.http.basic_task import UfoObjectGet,UfoObjectDelete
from cloudlib.restful.cloudfs.http.mission import Mission

def libUploadFile(atName,token,objPath,src='',handle=None,headers={}):

    ev = Mission(atName,token)
    t = FileUpload(objPath,src,handle,headers)
    t = ev.http(t)
    resp = t.response
    if '0' == resp['status']:
        msg = json.loads(resp['msg'])
        msg['permisson'] = msg['X-Object-Permisson']
        msg.pop('X-Object-Permisson')
        resp['msg'] = json.dumps(msg)
    return t.response

def libDownloadFile(atName,token,objPath): 

    ev = Mission(atName,token)
    t = FileDownload(objPath)
    t = ev.download(t)
    app_iter = t
    return app_iter

def libDeleteFile(atName,token,objPath):
    
    ev = Mission(atName,token)
    t = UfoObjectDelete(objPath)
    t = ev.http(t)
    return t.response
    
if __name__ == "__main__":

    email = 'zhu__feng001@163com'
    passwd = '123456'
    
    ev = TestMission(email,passwd)
#    print ev.getAtName()
    
    t = UfoObjectGet('/normal/test.txt')
#    t = FileMeta('/normal/test.txt')

#    t = QuotaMeta()

#    t = ev.http(t)   
    app_iter = ev.download(t) 
    for data in app_iter:
        print len(data)
        print data

