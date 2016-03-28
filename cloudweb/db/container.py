# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.table.stobj import account2id,insert_stobj,fullPath2id, \
    delete_stobj,id2childAttrs

def cntdelete(path,conn):
    # path /zhu__feng00000com/0/AUTH_zhu__feng00000com/%E6%B5%8B%20%E8%AF%95
    path = unquote(path)
    newPath = '/'.join(path.split('/')[3:])
    id = fullPath2id(conn,newPath) 
    return delete_stobj(conn,id)

def cntput(path,conn):

    path = unquote(path)
    newPath = '/'.join(path.split('/')[3:])
    aPath = newPath.split('/')[0]
    cPath = newPath.split('/')[-1]
    return insert_container(conn,cPath,aPath)

def cnthead(path,conn):
    
    return True,''

def cntmeta(path,conn):

    return True,''

def cntget(path,conn):

    return True,''

def cntpost(path,conn):

    return True,''

def insert_container(conn,stobj_path,abs_parent):

    parent_id = account2id(conn,abs_parent)
    if -1 == parent_id:
        return False,'fetch account id error'
    return insert_stobj(conn,'container',stobj_path,parent_id,'')

def cntList(db,atName,cntPath):
    
    newPath = '/'.join([atName,cntPath])
    id = fullPath2id(db, newPath)
    return id2childAttrs(db, id)

