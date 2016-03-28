# -*- coding: utf-8 -*-

import json
from cloudweb.events.events import TestEvent
from cloudweb.events.cloudfs import QuotaMeta,QuotaSet

def getAtQuota(ev):

    t = QuotaMeta()
    t = ev.http(t)
    resp = t.response
    if '0' == resp['status']:
        msg = json.loads(resp['msg'])
        msg['bytes-used'] = msg['X-Account-Bytes-Used']
        msg.pop('X-Account-Bytes-Used')
        msg['quota-bytes'] = msg['X-Account-Meta-Quota-Bytes']
        msg.pop('X-Account-Meta-Quota-Bytes')
        msg.pop('X-Timestamp')
        resp['msg'] = json.dumps(msg)
    return t.response

def setAtQuota(ev,val):
    
    t = QuotaSet(val)
    t = ev.http(t)
    return t.response
   
if __name__ == "__main__":

    email = 'zhu__feng001@163com'
    passwd = '123456'
    
    ev = TestEvent(email,passwd)
    print getAtQuota(ev)
    
#    print setAtQuota(ev, '0')
#    print getAtQuota(ev)
#    print setAtQuota(ev, str(1024*1024*1024))