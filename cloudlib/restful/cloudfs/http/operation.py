# -*- coding: utf-8 -*-
import json
from httplib import HTTPSConnection
from cloudweb.platform.globalx.static import CLOUDFS_HOST,CLOUDFS_PORT,CLOUDFS_CA_CRT,CLOUDFS_CA_KEY,HTTP_TIMEOUT
class Operation:
    
    def __init__(self):
        
        self.conn = None
        self.connection_flag = False
        self.response = {}
        
    def __enter__(self):
        self.connect()
        return self 
  
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
            
    def __exit__(self,type,value,trace):
        self.close()
        
    def http(self,t):
    
        self.conn.request(t.getMethod(),t.getUrl(),t.getBody(),t.getHeaders())
        resp = self.conn.getresponse()
        t.status = resp.status
        t.data = resp.read()
        
        if 2==t.status/100:
            if t.data:
                try:
                    msg = json.loads(t.data)
                    if type([]) == type(msg):
                        t.response = {'status':'0','msg':msg}
                    elif type({}) == type(msg) and msg.has_key('status'):
                        t.response = json.loads(t.data)
                    else:
                        t.response = {'status':'0','msg':t.data} 
                except:
                    t.response = {'status':'0','msg':t.data} 
                # try:
                #     msg = json.loads(t.data)
                #     t.response = {'status':'0','msg':msg}
                # except:
                #     t.response = {'status':'0','msg':t.data}
            else:
                t.response = {'status':'0','msg':t.data}
        else:
            try:
                msg = json.loads(t.data)
                t.response = msg
            except:
                t.response = {'status':'-1','msg':t.data}
                       
        return t
    
def getOperation():

    return Operation()

def execute(t):
    
    with getOperation() as op:
        op.http(t)
    
    return t 

