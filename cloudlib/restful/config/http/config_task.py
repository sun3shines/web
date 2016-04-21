# -*- coding: utf-8 -*-

import urllib
import json

from cloudlib.restful.config.http.task import Task
from cloudlib.urls.config import strConfigGet,strConfigSet,strExecutorPull

class ConfExecutorPull(Task):
    
    def getBody(self):
        return ''
    
    def getUrl(self):
        return strExecutorPull
    
class ConfConfigGet(Task):
    
    def getBody(self):
        return ''
    
    def getUrl(self):
        return strConfigGet
    
class ConfConfigSet(Task):
    
    def getBody(self):
        return ''
    
    def getUrl(self):
        return strConfigSet
    
         