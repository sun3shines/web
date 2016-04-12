# -*- coding: utf-8 -*-

# daemon data;server data ; sdata

from cloudweb.platform.cache import UserCache,TokenCache
class Server:
    
    def __init__(self):
        
        self.user = UserCache()
        self.token = TokenCache()
        