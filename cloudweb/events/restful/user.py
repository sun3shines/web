# -*- coding: utf-8 -*-

import json
import cloudweb.events.operation as operation

class TokenGet:

    def __init__(self,email,passwd):

        self.email = email
        self.passwd = passwd

    def getMethod(self):
        return 'POST'

    def getUrl(self):
        return '/oauth/access_token'

    def getBody(self):
        return json.dumps({'email':self.email,'password':self.passwd})

    def getHeaders(self):
        return {}

def getToken(email,passwd):

    t = TokenGet(email,passwd)
    t = operation.execute(t)
    return t.response

if __name__ == '__main__':

    email = 'zhu__feng001@163com'
    passwd = '123456'
    print getToken(email,passwd)
    