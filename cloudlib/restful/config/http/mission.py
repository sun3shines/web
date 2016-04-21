# -*- coding: utf-8 -*-

import json
from httplib import HTTPConnection
from cloudapi.globalx.static import HTTP_TIMEOUT

class Mission:
    
    def __init__(self,http_host,http_port):
        
        self.conn = None
        self.connection_flag = False
        self.readsize = 4096
        self.http_host = http_host
        self.http_port = http_port
        
    def __enter__(self):
        self.connect()
        return self 
  
    def getHttpsConn(self):
        
        return HTTPConnection(self.http_host,self.http_port,True,HTTP_TIMEOUT)  

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
       
        self.conn.request(t.getMethod(),t.getUrl(),t.getBody(),t.getHeaders())
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
 
def getMission(host,port):

    return Mission(host,port)

def execute(host,port,t):
    
    with getMission(host,port) as m:
        m.http(t)
    
    return t 

def download(host,port,t):
    m = getMission(host,port)
    return m.download(t)

