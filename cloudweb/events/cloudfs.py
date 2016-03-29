# -*- coding: utf-8 -*-

import urllib
import json

class Task:

    def __init__(self):
        self.execute = False
        self.response = {}

    def getPartialUrl(self):

        return ''

    def getParams(self):

        return {}

    def getBody(self):

        return ''

    def getMethod(self):

        return 'GET'

    def getHeaders(self):

        return {}

class ContainerList(Task):
    pass

class ContainerCreate(Task):
    def __init__(self,cnt):
        self.cnt = urllib.quote(cnt)
    def getMethod(self):
        return 'PUT'
    def getPartialUrl(self):
        return self.cnt
    
class ContainerDelete(Task):
    def __init__(self,cnt):
        self.cnt = urllib.quote(cnt)
        
    def getMethod(self):
        return 'DELETE'
    
    def getPartialUrl(self):
        return self.cnt
    
class ObjectList(Task):
    
    def __init__(self,cnt,r=False):
        self.cnt = urllib.quote(cnt)
        self.r = r
    def getParams(self):
        return {'op':'LISTDIR',
                'recursive':str(self.r).lower()}
        
    def getPartialUrl(self):
        return self.cnt
    
class ObjectCreate(Task):
    
    def __init__(self,obj,srcPath='',handle=None):
        self.obj = urllib.quote(obj)
        self.srcPath = urllib.quote(srcPath)
        self.handle = handle
    def getMethod(self):
        return 'PUT'
    
    def getPartialUrl(self):
        return self.obj
    
    def getBody(self):
        if self.srcPath:
            return open(self.srcPath)
        else:
            return self.handle

    
class ObjectDelete(Task):
    
    def __init__(self,obj):
        self.obj = urllib.quote(obj)
        
    def getPartialUrl(self):
        return self.obj
    
    def getMethod(self):
        return 'DELETE'
    
class ObjectCopy(Task):
    
    def __init__(self,obj ,dst):
        self.obj = urllib.quote(obj)
        self.dst = urllib.quote(dst)
        
    def getMethod(self):
        return 'COPY'
    
    def getPartialUrl(self):
        return self.obj
    def getHeaders(self):
        return {'Destination':self.dst}
    
class ObjectGet(Task):
    
    def __init__(self,obj):
        self.obj = urllib.quote(obj)
        
    def getPartialUrl(self):
        return self.obj
    
class QuotaMeta(Task):
    
    def getPartialUrl(self):
        return '/quota'
    
    def getParams(self):
        
        return {'op':'info',
                'type':'NORMAL'} 
    
class FileUpload(Task):
    
    def __init__(self,obj,src='',handle=None,headers={}):
        
        self.obj = urllib.quote(obj)
        self.src = urllib.quote(src)
        self.handle = handle
        self.headers = headers

    def getMethod(self):    
        return 'PUT'
    
    def getPartialUrl(self):
        
        return self.obj

    def getHeaders(self):
        return self.headers
    
    def getBody(self):
        if self.src:        
            return open(self.src)
        else:
            return self.handle

    def getParams(self):
        
        return {'op':'CREATE',
                'overwrite':'true',
                'type':'NORMAL',
                'metadata':'helloworld',
                'mode':'ENCRYPT',
                'storetype':'USER'
                }
        
class SegUpload(FileUpload):
    pass

class ManifestUpload(Task):
    
    def __init__(self,files,dst):
        
        self.files = files
        self.dst = urllib.quote(dst)
        
    def getHeaders(self):
        
        return {'X-Static-Large-Object':True}
    
    def getMethod(self):
        
        return 'PUT'
    
    def getPartialUrl(self):
        
        return '/normal/%s' % (self.dst)
    
    def getParams(self):
        
        return {'multipart-manifest':'put',
                'overwrite':'true'}
        
    def getBody(self):
        
        datas = []
        for x in self.files:
            datas.append({'path':x[0],'etag':x[1],'size_bytes':x[2]})
            
        return json.dumps(datas)
            
class DirCreate(Task):
    
    def __init__(self,direr):
        
        self.direr = urllib.quote(direr)
        
    def getMethod(self):
        return 'PUT'
    
    def getPartialUrl(self):
        return self.direr
    
    def getParams(self):
        return {'op':'MKDIRS',
                'ftype':'d',
                'type':'NORMAL'}
        
class FsDelete(Task):
    def __inti__(self,direr,ftype):
        self.direr = urllib.quote(direr)
        self.ftype = ftype
        
    def getMethod(self):
        return 'DELETE'
    
    def getPartialUrl(self):
        return self.direr
    def getParams(self):
        return {'op':'DELETE',
                'ftype':self.ftype,
                'recursive':'true',
                'type':'NORMAL',
                'cover':'true'}
 

class BatchDelete(Task):
    
    def __init__(self,files):
        self.files = files
        
    def getPartialUrl(self):
        return '/batch'
    
    def getParams(self):
        return {'p':'DELETE',
                'type':'NORMAL'}
    
    def getMethod(self):
        return 'POST'
    
    def getBody(self):
        
        datas = []
        for x in self.files:
            datas.append({"path":x[0],"ftype":x[1]})
        return json.dumps({'list':datas})
    

class FsMove(Task):
    def __init__(self,direr,dst,ftype):
        self.direr = urllib.quote(direr)
        self.dst = urllib.quote(dst)
        self.ftype = ftype
        
    def getMethod(self):
        return 'PUT'
    
    def getHeaders(self):
        return {'Destination':self.dst}
    
    def getPartialUrl(self):
        return self.direr
    
    def getParams(self):
        return {'op':'MOVE',
                'ftype':self.ftype,
                'type':'NORMAL'}
        
class BatchMove(Task):
    
    def __init__(self,files):
        self.files = files
        
    def getPartialUrl(self):
        return '/batch'
    
    def getMethod(self):
        return 'POST'
    
    def getParams(self):
        return {'op':'MOVE',
                'type':'NORMAL'}
    
    def getBody(self):
        datas = []
        for x in self.files:
            datas.append({"from":x[0],"to":x[1],"ftype":x[2]})
        return json.dumps({'list':datas})


class FsCopy(Task):
    
    def __init__(self,direr,dst,ftype):
        self.direr = urllib.quote(direr)
        self.dst = urllib.quote(dst)
        self.ftype =ftype
        
    def getMethod(self):
        return 'PUT'
    
    def getPartialUrl(self):
        return self.dier
    
    def getParams(self):
        return {'op':'COPY',
                'ftype':self.ftype,
                'type':'NORMAL'}
        
    def getHeaders(self):
        return {'Destination':self.dst}
    
class BatchCopy(Task):
    
    def __init__(self,files):
        self.files = files
        
    def getBody(self):
        datas = []
        for x in self.files:
            datas.append({"from":x[0],"to":x[1],"ftype":x[2]})
        return json.dumps({'list':datas})
    
    def getMethod(self):
        return 'POST'
    
    def getPartialUrl(self):
        return '/batch'
    def getParams(self):
        return {'op':'COPY',
                'type':'NORMAL'}
    
class FileGet(Task):
    
    def __init__(self,obj):
        self.obj = urllib.quote(obj)
        
    def getPartialUrl(self):
        return self.obj
    
    def getParams(self):
        return {'op':'OPEN',
                'offset':'0',
                'length':'10',
                'type':'NORMAL',
                'version':'LATEST',
                'mode':'NORMAL'}
        
class FileHistory(Task):
    def __init__(self,obj):
        self.obj = urllib.quote(obj)
        
    def getPartialUrl(self):
        
        return self.obj
    
    def getParams(self):
        return {'op':'GETHISTORY',
                'type':'NORMAL'}

class OpHistory(Task):

    def getParams(self):
        return {'op':'GET_OP_HISTORY',
                'recent':'10'}
           
class OpDelete(Task):
        
    def getParams(self):
        return {'op':'DELETE_HISTORY',
                'recent':'5'}

class LinkCreate(Task):
    def __init__(self,direr,dst):
        self.direr = urllib.quote(direr)
        self.dst = urllib.quote(dst)
        
    def getMethod(self):
        return 'PUT'
    
    def getPartialUrl(self):
        return self.direr
    
    def getParams(self):
        return {'op':'CREATESYMLINK',
                'destination':self.dst,
                'type':'NORMAL'}
    
class FsRename(Task):
    
    def __init__(self,direr,dst,ftype):
        self.direr =  urllib.quote(direr)
        self.dst = urllib.quote(dst)
        self.ftype = ftype
        
    def getParams(self):
        return {'op':'RENAME',
                'destination':self.dst,
                'ftype':self.ftype,
                'type':'NORMAL'}
        
    def getMethod(self):
        return 'PUT'
    
    def getPartialUrl(self):
        return self.direr
    
class FileMeta(Task):
    
    def __init__(self,obj):
        self.obj = urllib.quote(obj)
        
    def getPartialUrl(self):
        return self.obj
    
    def getParams(self):
        return {'op':'GETFILEATTR',
                'type':'NORMAL',
                'version':'LATEST'}
    
class RcyList(Task):
    
    def getPartialUrl(self):
        return '/recycle/user'
    
    def getParams(self):
        return {'op':'GETRECYCLER',
                'start':'0',
                'limit':'10',
                'type':'NORMAL'}
    

class RcyBatch(Task):
    
    def __init__(self,files):
        self.files = files
        
    def getMethod(self):
        return 'POST'
    
    def getBody(self):
        datas = []
        for x in self.files:
            datas.append({"uuid":x[0],"path":x[1],"ftype":x[2]})
            
        return json.dumps({"list":datas})
    
    def getParams(self):
        return {'op':'MOVERECYCLE',
                'type':'NORMAL',
                'overwrite':'true'}
        
    def getPartialUrl(self):
        return '/batch'
    
class RcyReset(Task):
    def getMethod(self):
        return 'POST'
    
    def getParams(self):
        return {'op':'RECYCLER',
                'type':'NORMAL'}
        
    def getPartialUrl(self):
        return '/clearrecycle'
    
class FilePermission(Task):
    
    def __init__(self,obj):
        self.obj = urllib.quote(obj)
        
    def getHeaders(self):
        return {'X-Object-Permisson': 500}
    
    def getMethod(self):
        return 'PUT'
    
    def getParams(self):
        return {'op':'SETPERMISSION',
                'type':'NORMAL'}
        
    def getPartialUrl(self):
        return self.obj
    
class FileList(Task):
    def __init__(self,cnt):
        self.cnt = urllib.quote(cnt)
    
    def getPartialUrl(self):
        return self.cnt
    
    def getParams(self):
        return {'op':'LISTDIR',
                'recursive':'true',
                'type':'NORMAL',
                'ftype':'d'}
    
class QuotaSet(Task):
    def __init__(self,qbytes):
        self.qbytes = qbytes
        
    def getHeaders(self):
        return {'X-Account-Meta-Quota-Bytes':self.qbytes}
    
    def getMethod(self):
        return 'POST'
    
    def getPartialUrl(self):
        return '/quota'
    
    def getParams(self):
        return {'op':'createstorage'}
    
class UserInit(Task):
    
    def getPartialUrl(self):
        return '/register'
    def getMethod(self):
        return 'PUT'
    
class SetVersions(Task):
    def __init__(self,vtest,versions):
        self.vtest = urllib.quote(vtest)
        self.versions = urllib.quote(versions)
    def getMethod(self):
        return 'POST'
    
    def getPartialUrl(self):
        return self.vtest
    def getHeaders(self):
        return {'X-Versions-Location': self.versions}
    
class AccountMeta(Task):
    
    def getMethod(self):
        return 'META'
    
class ContainerMeta(Task):
    def __init__(self,cnt):
        
        self.cnt = urllib.quote(cnt)
        
    def getPartialUrl(self):
        return self.cnt
    
    def getMethod(self):
        return 'META'

class SegsGet(ObjectGet):
    pass

class ManifestGet(Task):
    
    def __init__(self,obj):
        self.obj = urllib.quote(obj)
        
    def getParams(self):
        return {'multipart-manifest':'get'}
    
    def getPartialUrl(self):
        return self.obj

class SegsDelete(Task):
    
    def __init__(self,obj):
        self.obj = urllib.quote(obj)
        
    def getMethod(self):
        return 'DELETE'
    
    def getPartialUrl(self):
        return self.obj
    
    def getParams(self):
        return {'multipart-manifest':'delete'}
    
class ManifestDelete(ObjectDelete):
    pass
    
class QuotaRemove(Task):
    def getMethod(self):
        return 'POST'
    
    def getHeaders(self):
        return {'X-Remove-Account-Meta-Quota-Bytes': '1'}
    
class DirReset(Task):
    
    def __init__(self,direr):
        self.direr = urllib.quote(direr)
        
    def getMethod(self):
        return 'PUT'
    
    def getPartialUrl(self):
        return self.direr
    
    def getParams(self):
        return {'op':'RESET',
                'ftype':'d',
                'recursive':'true',
                'type':'NORMAL'}
    
    
class VerCreate(Task):
    
    def __init__(self,obj):
        self.obj = urllib.quote(obj)
        
    def getBody(self):
        return '1'
    
    def getParams(self):
        return {'overwrite':'true'}
    
    def getPartialUrl(self):
        return self.obj
    
    def getMethod(self):
        return 'PUT'
   
class FileDownload(ObjectGet):
    pass 
