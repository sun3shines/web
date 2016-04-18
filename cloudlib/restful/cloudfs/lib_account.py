# -*- coding: utf-8 -*-

from cloudlib.restful.cloudfs.http.mission import TestMission,Mission
from cloudlib.restful.cloudfs.http.basic_task import UfoAccountMeta
from cloudlib.restful.cloudfs.http.advanced_task import UserInit
    
def libGetAccountMeta(atName,token):
    
    ev = Mission(atName,token)
    t = UfoAccountMeta()
    t = ev.http(t)
    return t.response

if __name__ == "__main__":

    email = 'testadministrator@163com'
    passwd = '123456'
    
    ev = TestMission(email,passwd)
    print ev.getAtName()
#    t = AccountMeta()
    t = UserInit()
#    t = FileUpload('/normal/test.txt','/root/install.log')
#    t = FileMeta('/normal/test.txt')
#    t = DirCreate('/normal/dir')
#    t = ObjectList('/normal',r=True) 
    t = ev.http(t)
    print t.response

