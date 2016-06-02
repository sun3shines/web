
import json
from cloudapi.missions.tasks.task import Task
from cloudlib.urls.flask import strObjectDetails, strDisableObject, strEnableObject, strDeleteObject, strDownloadObject, strUploadObject
class ObjectDisable(Task):
    def __init__(self, atName, objPath):
        self.atName = atName
        self.objPath = objPath

    def getUrl(self):
        return strDisableObject

    def getBody(self):
        return json.dumps({'atName': self.atName, 'objPath': self.objPath})

class ObjectEnable(Task):
    def __init__(self, atName, objPath):
        self.atName = atName
        self.objPath = objPath

    def getUrl(self):
        return strEnableObject

    def getBody(self):
        return json.dumps({'atName': self.atName, 'objPath': self.objPath})

class ObjectDelete(Task):
    def __init__(self, atName, objPath):
        self.atName = atName
        self.objPath = objPath

    def getUrl(self):
        return strDeleteObject

    def getBody(self):
        return json.dumps({'atName': self.atName, 'objPath': self.objPath})

class ObjectDownload(Task):
    def __init__(self, atName, objPath):
        self.atName = atName
        self.objPath = objPath

    def getUrl(self):
        return strDownloadObject

    def getBody(self):
        return json.dumps({'atName': self.atName, 'objPath': self.objPath})

class ObjectUpload(Task):
    def __init__(self, atName, obj, path_or_file):
        self.atName = atName
        if isinstance(obj, unicode):    # pay attention to chinese
            obj = obj.encode('utf-8')
        self.obj = obj
        #self.localPath = localPath

        self.localPath = None
        self.file = None
        if isinstance(path_or_file, (str, unicode)):
        # path
            if isinstance(path_or_file, unicode):
                path_or_file = path_or_file.encode('utf-8')
            self.localPath = path_or_file
        else:
            # file-like IO object: check needed interfaces
            assert hasattr(path_or_file, '__len__') or hasattr(path_or_file, 'fileno')
            assert hasattr(path_or_file, 'read')
            self.file = path_or_file

    def getUrl(self):
        return strUploadObject

    def getParams(self):
        return {'atName': self.atName, 'objPath': self.obj}

    def getBody(self):
        if self.localPath:
            return file(self.localPath)
        else:
            assert self.file, "both file and local path are none"
            return self.file



