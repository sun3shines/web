# -*- coding: utf-8 -*-

import json
from cloudweb.events.events import TestEvent
from cloudweb.events.cloudfs import FileUpload,FileDownload,ObjectGet,\
    ObjectDelete

def uploadFile(ev,objPath,src='',handle=None,headers={}):

    t = FileUpload(objPath,src,handle,headers)
    t = ev.http(t)
    resp = t.response
    if '0' == resp['status']:
        msg = json.loads(resp['msg'])
        msg['permisson'] = msg['X-Object-Permisson']
        msg.pop('X-Object-Permisson')
        resp['msg'] = json.dumps(msg)
    return t.response

def downloadFile(ev,objPath): 

    t = FileDownload(objPath)
    t = ev.download(t)
    app_iter = t
    return app_iter

def deleteFile(ev,objPath):
    
    t = ObjectDelete(objPath)
    t = ev.http(t)
    return t.response
    
if __name__ == "__main__":

    email = 'zhu__feng001@163com'
    passwd = '123456'
    
    ev = TestEvent(email,passwd)
#    print ev.getAtName()
    
    t = ObjectGet('/normal/test.txt')
#    t = FileMeta('/normal/test.txt')

#    t = QuotaMeta()

#    t = ev.http(t)   
    app_iter = ev.download(t) 
    for data in app_iter:
        print len(data)
        print data


    
    
