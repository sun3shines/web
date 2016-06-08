# -*- coding: utf-8 -*-

from eventlet import  sleep

from cloudweb.platform.drive.utils import cloudfsGetAtName,flaskGetAtName,getUserToken,validUser
from cloudweb.platform.globalx.variable import GLOBAL_USER_CONSISTENCY,USER_CONSISTENCY_DIR,GLOBAL_USER_DB
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.platform.tools.init_consistency_db import getDirList
from cloudweb.platform.thread.worker import do_consistency_worker
from cloudweb.db.table.lock.mysql import getlock
def db_consistent(func):
    
    def wrapper(*args,**kwargs):
        request = args[0]
        flag,msg = cloudfsGetAtName(request)
        if not flag:
            return jresponse('-1', msg, request, 400)
         
        atName = msg
        if GLOBAL_USER_CONSISTENCY.success(atName):
            return func(*args,**kwargs)
        
        elif GLOBAL_USER_CONSISTENCY.running(atName):
            USER_CONSISTENCY_DIR.put_consistency(atName)
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
        request = args[0]
        atName = flaskGetAtName(request)
        if GLOBAL_USER_CONSISTENCY.running(atName):    
            while GLOBAL_USER_CONSISTENCY.running(atName):
                print 'consistent loop'
                sleep(5)
              
        if GLOBAL_USER_CONSISTENCY.success(atName):
            return func(*args,**kwargs)
        
        flag,resp = getUserToken(atName, request)
        if not flag:
            if request.GET.get('x_admin_token'):
                print 'user with admin token'
                resp = request.GET.get('x_admin_token')
                print '1',atName,resp
            else:
                return resp
            
        usertoken = resp
        if not validUser(atName, usertoken):
            return jresponse('-1', 'user does not login,please login', request, 400)
        
        conn = GLOBAL_USER_DB.get(atName) 
        print '2',atName,resp 

        GLOBAL_USER_CONSISTENCY.put(atName, GLOBAL_USER_CONSISTENCY.state_running)
        with getlock(conn) as mylock:
            flag,msg = getDirList(conn, atName, usertoken, 0)
            if not flag:
                GLOBAL_USER_CONSISTENCY.eliminate(atName)
                return jresponse('-1', msg, request, 400)
        
        GLOBAL_USER_CONSISTENCY.put(atName, GLOBAL_USER_CONSISTENCY.state_success)
        return func(*args,**kwargs)
    
    return wrapper
