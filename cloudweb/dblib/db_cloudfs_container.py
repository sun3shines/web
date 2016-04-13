# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.db_container import insert_container
from cloudweb.db.table.stobj import fullPath2id,delete_stobj

# cntdelete -> db_cloudfs_container_delete
# cntput -> db_cloudfs_container_put
# cnthead -> db_cloudfs_container_head
# cntmeta -> db_cloudfs_container_meta
# cntget -> db_cloudfs_container_get
# cntpost -> db_cloudfs_container_post

def db_cloudfs_container_delete(newPath,conn):
    
    # path /zhu__feng00000com/0/AUTH_zhu__feng00000com/%E6%B5%8B%20%E8%AF%95
    # path = unquote(path)
    # newPath = '/'.join(path.split('/')[3:])
    
    cid = fullPath2id(conn,newPath) 
    return delete_stobj(conn,cid)

def db_cloudfs_container_put(newPath,conn):

    # path = unquote(path)
    # newPath = '/'.join(path.split('/')[3:])
    
    aPath = newPath.split('/')[0]
    cPath = newPath.split('/')[-1]
    return insert_container(conn,cPath,aPath)

def db_cloudfs_container_head(path,conn):
    
    return True,''

def db_cloudfs_container_meta(path,conn):

    return True,''

def db_cloudfs_container_get(path,conn):

    return True,''

def db_cloudfs_container_post(path,conn):

    return True,''