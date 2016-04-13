# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.db_dir import insert_dir
from cloudweb.db.table.stobj import fullPath2id,delete_stobj,delete_child_stobj,move_stobj,copy_stobj

# drdelete
# drreset
# drdeleteRecycle
# drmoveRecycle
# drput
# drmove
# drcopy
# drmetaGet
# drget

def db_cloudfs_dir_delete(newPath,conn):

#     path = unquote(path)
#    newPath = '/'.join(path.split('/')[3:])
    did = fullPath2id(conn,newPath)
    return delete_stobj(conn,did)

def db_cloudfs_dir_reset(newPath,conn):

#     path = unquote(path)
#     newPath = '/'.join(path.split('/')[3:])
    did = fullPath2id(conn,newPath)

    return delete_child_stobj(conn,did)

def db_cloudfs_dir_deleterecycle(srcNewPath,dstNewPath,conn):

    # srcNewPath = unquote(srcNewPath)
    # dstNewPath = unquote(dstNewPath)

    return move_stobj(conn,srcNewPath,dstNewPath)

def db_cloudfs_dir_moverecycle(srcNewPath,dstNewPath,conn):

    return db_cloudfs_dir_deleterecycle(srcNewPath,dstNewPath,conn)

def db_cloudfs_dir_put(newPath,conn):

    # path = unquote(path)
    # newPath = '/'.join(path.split('/')[3:]) 
    return insert_dir(conn,newPath)

def db_cloudfs_dir_move(srcNewPath,dstNewPath,conn):
    
    return db_cloudfs_dir_deleterecycle(srcNewPath,dstNewPath,conn)

def db_cloudfs_dir_copy(srcNewPath,dstNewPath,conn):

    # srcNewPath = unquote(srcNewPath)
    # dstNewPath = unquote(dstNewPath)
    
    return copy_stobj(conn,srcNewPath,dstNewPath)

def db_cloudfs_dir_metaget(path):

    return True,''

def db_cloudfs_dir_get(path):

    return True,''
