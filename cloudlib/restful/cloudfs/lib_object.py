
from cloudlib.restful.cloudfs.http.advanced_task import FileMeta
from cloudlib.restful.cloudfs.http.mission import Mission

def libGetObjectMeta(atName,token,path):
    
    ev = Mission(atName,token)
    t = FileMeta(path)
    t = ev.http(t)
    return t.response
