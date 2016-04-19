# -*- coding: utf-8 -*-

import time

from cloudweb.drive.utils import cloudfsGetAtName,flaskGetAtName,getUserToken
from cloudweb.globalx.variable import GLOBAL_USER_CONSISTENCY,GLOBAL_USER_TOKEN,GLOBAL_USER_DB
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.tools.init_consistency_db import getDirList
from cloudweb.thread.worker import do_consistency_worker

def db_consistent(func):
    
    def wrapper(*args,**kwargs):
        import pdb;pdb.set_trace()
        request = args[0]
        flag,msg = cloudfsGetAtName(request)
        if not flag:
            return jresponse('-1', msg, request, 400)
         
        atName = msg
        if GLOBAL_USER_CONSISTENCY.success(atName):
            return func(*args,**kwargs)
        
        elif GLOBAL_USER_CONSISTENCY.running(atName):
            return jresponse('0',GLOBAL_USER_CONSISTENCY.state_running,request,200)
         
        flag,resp = getUserToken(atName, request)
        if not flag:
            return resp
        
        usertoken = resp
        
        do_consistency_worker(atName,usertoken).start()
        
        return jresponse('0',GLOBAL_USER_CONSISTENCY.state_running,request,200)
    
    return wrapper

def flask_consistent(func):
    
    def wrapper(*args,**kwargs):
        import pdb;pdb.set_trace() 
        request = args[0]
        atName = flaskGetAtName(request)
        
        if GLOBAL_USER_CONSISTENCY.running(atName):    
            while GLOBAL_USER_CONSISTENCY.running(atName):
                time.sleep(5)
               
        if GLOBAL_USER_CONSISTENCY.success(atName):
            return func(*args,**kwargs)
        
        flag,resp = getUserToken(atName, request)
        if not flag:
            return resp
        
        usertoken = resp
        
        conn = GLOBAL_USER_DB.get(atName) 
        GLOBAL_USER_CONSISTENCY.put(atName, GLOBAL_USER_CONSISTENCY.state_running)
        
        flag,msg = getDirList(conn, atName, usertoken, 0)
        if not flag:
            return jresponse('-1', msg, request, 400)
        
        GLOBAL_USER_CONSISTENCY.put(atName, GLOBAL_USER_CONSISTENCY.state_success)
        return func(*args,**kwargs)
    
    return wrapper
