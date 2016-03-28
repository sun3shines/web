# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.table.stobj import insert_object

def lkput(path,conn):
    
    path = unquote(path)
    newPath = '/'.join(path.split('/')[3:])
    return insert_link(conn,newPath)

def insert_link(conn,absPath,stobj_state = 'enable'): 

    stobj_path,abs_parent = conn.splitPath(absPath) 
    return insert_object(conn,'link',stobj_path,abs_parent,stobj_state)


    
