# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.table.stobj import fullPath2id,delete_stobj,move_stobj,copy_stobj
from cloudweb.db.db_object import insert_file

# otput -> db_cloudfs_object_put
# otget -> db_cloudfs_object_get
# othead -> db_cloudfs_object_head
# otmeta -> db_cloudfs_object_meta
# otdelete -> db_cloudfs_object_delete
# otdeleteRecycle -> db_cloudfs_object_deleterecycle
# otcopy -> db_cloudfs_object_copy
# otmove -> db_cloudfs_object_move
# otmoveRecycle -> db_cloudfs_object_moverecycle
# otpost -> db_cloudfs_object_post

def db_cloudfs_object_put(newPath,conn):
    
    # path = unquote(path)

    # newPath = '/'.join(path.split('/')[3:])
    return insert_file(conn,newPath)

def db_cloudfs_object_get(path):

    return True,''

def db_cloudfs_object_head(path):
    
    return True,''

def db_cloudfs_object_meta(path):

    return True,''

def db_cloudfs_object_delete(newPath,conn):

    # path = unquote(path)

    # newPath = '/'.join(path.split('/')[3:])
    oid = fullPath2id(conn,newPath)
    return delete_stobj(conn,oid)

def db_cloudfs_object_deleterecycle(srcNewPath,dstNewPath,conn):

    # srcNewPath = unquote(srcNewPath)
    # dstNewPath = unquote(dstNewPath)

    return move_stobj(conn,srcNewPath,dstNewPath)

def db_cloudfs_object_copy(srcNewPath,dstNewPath,conn):
    
    # srcNewPath = unquote(srcNewPath)
    # dstNewPath = unquote(dstNewPath)
    return copy_stobj(conn,srcNewPath,dstNewPath)

def db_cloudfs_object_move(srcNewPath,dstNewPath,conn):

    return db_cloudfs_object_deleterecycle(srcNewPath,dstNewPath,conn) 
   
def db_cloudfs_object_moverecycle(srcNewPath,dstNewPath,conn):

    return db_cloudfs_object_deleterecycle(srcNewPath,dstNewPath,conn)

def db_cloudfs_object_post(path):

    return True,''
