# -*- coding: utf-8 -*-

from urllib import unquote

from cloudweb.db.table.stobj import account2id,insert_stobj,delete_stobj,update_stobj,\
    id2childAttrs
    
from cloudweb.db.table.mysql import getDb

def atdelete(path,conn):

    path = unquote(path)
    newPath = '/'.join(path.split('/')[3:])
    id = account2id(conn,newPath)
    return delete_stobj(conn,id)

def atput(path,conn):

    path = unquote(path)
    newPath = '/'.join(path.split('/')[3:])
    return insert_account(conn,newPath)

def atexists(path,conn):

    # /v1/AUTH_zhu__feng00000com/register
    path = unquote(path)
    newPath = path.split('/')[2]
    return account_exists(conn,newPath)

def athead(path):

    return True,''

def atmeta(path):

    return True,''

def atget(path):

    return True,''

def atpost(path):
  
    return True,''

def account_exists(conn,path):

    if -1 != account2id(conn,path):
        return True
    return False

def insert_account(conn,stobj_path):

    return insert_stobj(conn,'account',stobj_path,'','enable')

def atEnable(db,path):
    
    id = account2id(db, path)
    return update_stobj(db,id,state='enable')

def atDisable(db,path):
    
    id = account2id(db,path)
    return update_stobj(db, id, state='disable')

def atList(db,path):
    id = account2id(db,path)
    return id2childAttrs( db,id)

if __name__ == '__main__':

    db = getDb()
#    atDisable(db,'AUTH_zhu__feng00000com')
    atEnable(db,'AUTH_zhu__feng00000com')

