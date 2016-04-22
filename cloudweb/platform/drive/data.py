# -*- coding: utf-8 -*-

# daemon data;server data

from cloudweb.platform.drive.cache import UserCache,TokenCache
class Server:
    
    def __init__(self):
        
        self.user = UserCache()
        self.token = TokenCache()
        