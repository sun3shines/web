# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.db_account import account2id,delete_stobj,insert_account,account_exists

# atdelete -> db_cloudfs_account_delete
# atput -> db_cloudfs_account_put
# atexists -> db_cloudfs_account_exists
# athead -> db_cloudfs_account_head
# atmeta -> db_cloudfs_account_meta
# atget -> db_cloudfs_account_get
# atpost -> db_cloudfs_account_post

def db_cloudfs_account_delete(newPath,conn):
    
    aid = account2id(conn,newPath)
    return delete_stobj(conn,aid)
    
def db_cloudfs_account_put(newPath,conn):

    return insert_account(conn,newPath)

def db_cloudfs_account_exists(newPath,conn):

    return account_exists(conn,newPath)

def db_cloudfs_account_head(path):

    return True,''

def db_cloudfs_account_meta(path):

    return True,''

def db_cloudfs_account_get(path):

    return True,''

def db_cloudfs_account_post(path):
  
    return True,''