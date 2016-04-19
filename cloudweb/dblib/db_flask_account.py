# -*- coding: utf-8 -*-

from cloudweb.db.db_account import account2id
from cloudweb.db.table.stobj import update_stobj,id2childAttrs
# from cloudweb.db.table.mysql import getDb

# atEnable -> db_flask_account_enable
# atDisable -> db_flask_account_disable
# atList -> db_flask_account_list

def db_flask_account_enable(db,path):
    
    aid = account2id(db, path)
    return update_stobj(db,aid,state='enable')

def db_flask_account_disable(db,path):
    
    aid = account2id(db,path)
    return update_stobj(db, aid, state='disable')

def db_flask_account_list(db,path):
    aid = account2id(db,path)
    return id2childAttrs( db,aid)

if __name__ == '__main__':
    pass
#    db = getDb()
#    atDisable(db,'AUTH_zhu__feng00000com')
#    atEnable(db,'AUTH_zhu__feng00000com')
