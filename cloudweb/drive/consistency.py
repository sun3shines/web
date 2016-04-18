
import json
from cloudweb.drive.utils import getAtName,getUserToken
from cloudweb.globalx.variable import GLOBAL_USER_CONSISTENCY,GLOBAL_USER_TOKEN
from cloudlib.common.bufferedhttp import jresponse
from cloudlib.restful.cloudfs.lib_container import libGetContainerList
from cloudlib.restful.cloudfs.lib_object import libGetObjectList
def db_consistent(func):
    
    def wrapper(*args,**kwargs):
        request = args[1]
        flag,msg = getAtName(request)
        if not flag:
            return jresponse('-1', msg, request, 400)
         
        atName = msg
        if GLOBAL_USER_CONSISTENCY.successed(atName):
            return func(*args,**kwargs)
        
        elif GLOBAL_USER_CONSISTENCY.waiting(atName):
            return jresponse('0',GLOBAL_USER_CONSISTENCY.running,request,200)
         
        flag,resp = getUserToken(atName, request)
        if not flag:
            return resp
        
        token = resp 
        flag,resp = user_consistency(atName, token,request)
        if not flag:
            return resp
        return func(*args,**kwargs)
    
    return wrapper



def user_consistency(atName,token,request):
    
    GLOBAL_USER_CONSISTENCY.put(atName, GLOBAL_USER_CONSISTENCY.running)
    lresp = libGetContainerList(atName,token)
    if '-1' == lresp['status']:
        GLOBAL_USER_CONSISTENCY.eliminate(atName)
        return False,jresponse('-1',lresp.get('msg'),request,400)
    
    container_list = json.loads(lresp.get('msg'))
    for container in container_list:
        container_path = '/'.join(['',container.get('name').encode('utf-8')])
        oresp = libGetObjectList(atName,token,container_path)
        if '-1' == oresp['status']:
            GLOBAL_USER_CONSISTENCY.eliminate(atName)
            return False,jresponse('-1',oresp.get('msg'),request,400)
        object_list = json.loads(oresp.get('msg'))
    pass
    
