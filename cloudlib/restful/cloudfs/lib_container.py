
from cloudlib.restful.cloudfs.http.advanced_task import FileMeta
from cloudlib.restful.cloudfs.http.basic_task import UfoContainerMeta
from cloudlib.restful.cloudfs.http.mission import Mission

def libGetContainerMeta(atName,token,path):
    
    ev = Mission(atName,token)
    t = UfoContainerMeta(path)
    t = ev.http(t)
    return t.response