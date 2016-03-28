# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.table.stobj import insert_object,fullPath2id,copy_stobj,move_stobj, \
    delete_stobj,delete_child_stobj,update_stobj

def otput(path,conn):
    
    path = unquote(path)

    newPath = '/'.join(path.split('/')[3:])
    return insert_file(conn,newPath)

def otget(path):

    return True,''

def othead(path):
    
    return True,''

def otmeta(path):

    return True,''

def otdelete(path,conn):

    path = unquote(path)

    newPath = '/'.join(path.split('/')[3:])
    id = fullPath2id(conn,newPath)
    return delete_stobj(conn,id)

def otdeleteRecycle(srcNewPath,dstNewPath,conn):

    srcNewPath = unquote(srcNewPath)
    dstNewPath = unquote(dstNewPath)

    return move_stobj(conn,srcNewPath,dstNewPath)

def otcopy(srcNewPath,dstNewPath,conn):
    
    srcNewPath = unquote(srcNewPath)
    dstNewPath = unquote(dstNewPath)
    return copy_stobj(conn,srcNewPath,dstNewPath)

def otmove(srcNewPath,dstNewPath,conn):

    return otdeleteRecycle(srcNewPath,dstNewPath,conn) 
   
def otmoveRecycle(srcNewPath,dstNewPath,conn):

    return otdeleteRecycle(srcNewPath,dstNewPath,conn)

def otpost(path):

    return True,''
 
def insert_file(conn,absPath,stobj_state = 'enable'):

    stobj_path,abs_parent = conn.splitPath(absPath) 
    return insert_object(conn,'file',stobj_path,abs_parent,stobj_state)

def disableOt(db,newPath):

    # objPath 为restful时，则为/normal/test.txt
    # objPath 为db时，则为 account/normal/test.txt ?? search 时有db操作。但是不是路径。
    
    id = fullPath2id(db,newPath)
    return update_stobj(db,id,state='disable')

def enableOt(db,newPath):
    
    id = fullPath2id(db,newPath)
    return update_stobj(db,id,state='enable')
