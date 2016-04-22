# -*- coding: utf-8 -*-

import threading
from cloudweb.platform.globalx.variable import GLOBAL_USER_CONSISTENCY,GLOBAL_USER_DB,GLOBAL_USER_TOKEN,USER_CONSISTENCY_DIR
from cloudweb.platform.tools.init_consistency_db import getDirList
from cloudweb.db.table.lock.mysql import getlock

class do_consistency_worker(threading.Thread):
    
    def __init__(self,atName,usertoken):
        threading.Thread.__init__(self)
        self.atName = atName
        self.usertoken = usertoken

    def run(self):
        
        print 'START DO CONSISTENCY WORKER THREAD' 
        while True:
            conn = GLOBAL_USER_DB.get(self.atName) 
            GLOBAL_USER_CONSISTENCY.put(self.atName, GLOBAL_USER_CONSISTENCY.state_running)
            with getlock(conn) as mylock:
                flag,_ = getDirList(conn, self.atName, self.usertoken, 0)
                if not flag:
                    GLOBAL_USER_TOKEN.eliminate(self.atName)
                    GLOBAL_USER_CONSISTENCY.eliminate(self.atName)
        
            if not USER_CONSISTENCY_DIR.get_consistency(self.atName):
                GLOBAL_USER_CONSISTENCY.put(self.atName, GLOBAL_USER_CONSISTENCY.state_success)
                print 'FINISH DO CONSISTENCY WORKER THREAD'
                break
            print 'LOOP DO CONSISTENCY WORKER THREAD'
            
