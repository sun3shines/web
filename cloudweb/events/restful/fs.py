# -*- coding: utf-8 -*-

import json
from cloudweb.events.events import TestEvent
from cloudweb.events.cloudfs import FileMeta,ContainerMeta,AccountMeta
from cloudweb.events.cloudfs import DirCreate,ObjectList
from cloudweb.events.cloudfs import UserInit

def getObjectMeta(path,ev):
    
    t = FileMeta(path)
    t = ev.http(t)
    return t.response

def getContainerMeta(path,ev):
    
    t = ContainerMeta(path)
    t = ev.http(t)
    return t.response
    
def getAccountMeta(ev):
    
    t = AccountMeta()
    t = ev.http(t)
    return t.response

if __name__ == "__main__":

    email = 'testadministrator@163com'
    passwd = '123456'
    
    ev = TestEvent(email,passwd)
    print ev.getAtName()
#    t = AccountMeta()
    t = UserInit()
#    t = FileUpload('/normal/test.txt','/root/install.log')
#    t = FileMeta('/normal/test.txt')
#    t = DirCreate('/normal/dir')
#    t = ObjectList('/normal',r=True) 
    t = ev.http(t)
    print t.response

