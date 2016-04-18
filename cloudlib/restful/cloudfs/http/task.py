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

