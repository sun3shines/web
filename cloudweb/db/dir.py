# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.table.stobj import insert_object,fullPath2id,delete_child_stobj, \
    delete_stobj,move_stobj,copy_stobj,id2childAttrs,id2treeAttrs

def drdelete(path,conn):

    path = unquote(path)
    newPath = '/'.join(path.split('/')[3:])
    id = fullPath2id(conn,newPath)
    return delete_stobj(conn,id)

def drreset(path,conn):

    path = unquote(path)
    newPath = '/'.join(path.split('/')[3:])
    id = fullPath2id(conn,newPath)

    return delete_child_stobj(conn,id)

def drdeleteRecycle(srcNewPath,dstNewPath,conn):

    srcNewPath = unquote(srcNewPath)
    dstNewPath = unquote(dstNewPath)

    return move_stobj(conn,srcNewPath,dstNewPath)

def drmoveRecycle(srcNewPath,dstNewPath,conn):

    return drdeleteRecycle(srcNewPath,dstNewPath,conn)

def drput(path,conn):

    path = unquote(path)
    newPath = '/'.join(path.split('/')[3:]) 
    return insert_dir(conn,newPath)

def drmove(srcNewPath,dstNewPath,conn):
    
    return drdeleteRecycle(srcNewPath,dstNewPath,conn)

def drcopy(srcNewPath,dstNewPath,conn):

    srcNewPath = unquote(srcNewPath)
    dstNewPath = unquote(dstNewPath)
    return copy_stobj(conn,srcNewPath,dstNewPath)

def drmetaGet(path):

    return True,''

def drget(path):

    return True,''

def insert_dir(conn,absPath):

    stobj_path,abs_parent = conn.splitPath(absPath) 
    return insert_object(conn,'dir',stobj_path,abs_parent,'')

def drList(db,atName,drPath,tree):
    newPath = '/'.join([atName,drPath])
    id = fullPath2id(db,newPath)
    if 'true' == tree:
        return id2treeAttrs(db, id)
    else:
        return id2childAttrs(db, id)

