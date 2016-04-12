# -*- coding: utf-8 -*-

import urllib
import json

from httplib import HTTPSConnection
from cloudweb.events.restful.user import getToken
from cloudweb.db.table.mysql import getDb
from cloudweb.globalx.static import CLOUDFS_HOST,CLOUDFS_PORT,CLOUDFS_CA_CRT,CLOUDFS_CA_KEY,HTTP_TIMEOUT
class Event:
    
    def __init__(self,email='',passwd='',sdata=None):
        
        self.connection_flag = False
        self.conn = None
        self.email = email
        self.passwd = passwd
        self.sdata = sdata
        self.db = getDb()

        self.readsize = 4096
        
    def getHttpsConn(self):
        
        return HTTPSConnection(CLOUDFS_HOST,CLOUDFS_PORT,CLOUDFS_CA_KEY,CLOUDFS_CA_CRT,True,HTTP_TIMEOUT)  

    def connect(self):
        
        if not self.connection_flag:
            self.conn = self.getHttpsConn()
            self.connection_flag = True
 
    def close(self):
        
        if self.connection_flag:
            self.conn.close()
            self.connection_flag = False
    
    def getAtName(self):

        return 'AUTH_' + self.email.replace('@','').replace('.','') 

    def getUrl(self):
        return '/'.join(['','v1',self.getAtName()])    

    def getHeaders(self):

        token = self.getToken()
        return {'X-Auth-Token':token}
    
    def getToken(self):
        
        return self.sdata.token.getToken(self.getAtName())
    
    def http(self,t):

        self.connect()
        
        url = self.getUrl() + t.getPartialUrl()
        ps = t.getParams() 
        if ps:
            url = url + '?' + urllib.urlencode(ps)

        headers = t.getHeaders()
        headers.update(self.getHeaders())
        self.conn.request(t.getMethod(),url,t.getBody(),headers)

        resp = self.conn.getresponse()
        t.status = resp.status
        t.data = resp.read()
        
        if 2==t.status/100:
            if t.data:
                msg = json.loads(t.data)
                if  msg.has_key('status'):
                    t.response = json.loads(t.data)
                else:
                    t.response = {'status':'0','msg':t.data}
            else:
                t.response = {'status':'0','msg':t.data}
        else:
            try:
                msg = json.loads(t.data)
                t.response = msg
            except:
                t.response = {'status':'-1','msg':t.data}
                       
        self.close()
 
        return t


    def download(self,t):
        try:
            self.connect()
  
            url = self.getUrl() + t.getPartialUrl()
            ps = t.getParams()
            if ps:
                url = url + '?' + urllib.urlencode(ps)

            headers = t.getHeaders()
            headers.update(self.getHeaders())
            self.conn.request(t.getMethod(),url,t.getBody(),headers)

            resp = self.conn.getresponse()
            while True:
                data = resp.read(self.readsize)
                if data:
                    yield data 
                else:
                    break
        finally:
            self.close()

class TestEvent(Event):

    def getToken(self):

        resp = getToken(self.email,self.passwd)
        if '-1' == resp['status']:
            return None

        return json.loads(resp['msg']).get('access_token') 

