# -*- coding: utf-8 -*-

import urllib
import json
from httplib import HTTPConnection
import cloudapi.globalx.static as api_globals

class Mission:
    
    def __init__(self):
        
        self.conn = None
        self.connection_flag = False
        self.readsize = 4096
 
    def __enter__(self):
        self.connect()
        return self 
  
    def getHttpsConn(self):
        
        return HTTPConnection(api_globals.CLOUD_PLATFORM_HOST,api_globals.CLOUD_PLATFORM_PORT,True,api_globals.HTTP_TIMEOUT)  

    def connect(self):
        
        if not self.connection_flag:
            self.conn = self.getHttpsConn()
            self.connection_flag = True
    
    def close(self):
        
        if self.connection_flag:
            self.conn.close()
            self.connection_flag = False
            
    def __exit__(self,type,value,trace):
        self.close()
        
    def http(self,t):
       
        url = t.getUrl()
        ps = t.getParams() 
        if api_globals.X_ADMIN_TOKEN:
            ps.update({'x_admin_token':api_globals.X_ADMIN_TOKEN})
        if ps:
            url = url + '?' + urllib.urlencode(ps)
            
        self.conn.request(t.getMethod(),url,t.getBody(),t.getHeaders())
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
                       
        return t
   
    def download(self,t):
        try:    
            self.connect()
            self.conn.request(t.getMethod(),t.getUrl(),t.getBody(),t.getHeaders())
            resp = self.conn.getresponse()
            while True:
                data = resp.read(self.readsize)
                if data:
                    yield data
                else:
                    break
        finally:
            self.close()
 
def getMission():

    return Mission()

def execute(t):
    
    with getMission() as m:
        m.http(t)
    
    return t 

def download(t):
    m = getMission()
    return m.download(t)

