# -*- coding: utf-8 -*-

import threading
from cloudweb.globalx.variable import GLOBAL_USER_CONSISTENCY,GLOBAL_USER_DB,GLOBAL_USER_TOKEN
from cloudweb.tools.init_consistency_db import getDirList

class do_consistency_worker(threading.Thread):
    
    def __init__(self,atName,usertoken):
        threading.Thread.__init__(self)
        self.atName = atName
        self.usertoken = usertoken

    def run(self):
        conn = GLOBAL_USER_DB.get(self.atName) 
        GLOBAL_USER_CONSISTENCY.put(self.atName, GLOBAL_USER_CONSISTENCY.state_running)
        
        flag,_ = getDirList(conn, self.atName, self.usertoken, 0)
        if not flag:
            GLOBAL_USER_TOKEN.eliminate(self.atName)
            GLOBAL_USER_CONSISTENCY.eliminate(self.atName)
        else:
            GLOBAL_USER_CONSISTENCY.put(self.atName, GLOBAL_USER_CONSISTENCY.state_success)       
        