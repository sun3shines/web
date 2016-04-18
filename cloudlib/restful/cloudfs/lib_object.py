
from cloudlib.restful.cloudfs.http.advanced_task import FileMeta
from cloudlib.restful.cloudfs.http.mission import Mission
from cloudlib.restful.cloudfs.http.basic_task import UfoObjectList

def libGetObjectList(atName,token,cnt):
    
    ev = Mission(atName,token)
    t = UfoObjectList(cnt,r=True)
    t = ev.http(t)
    return t.response

def libGetObjectMeta(atName,token,path):
    
    ev = Mission(atName,token)
    t = FileMeta(path)
    t = ev.http(t)
    return t.response
