# -*- coding: utf-8 -*-

from cloudweb.db.table.stobj import insert_object,fullPath2id

def insert_dir(conn,absPath):

    did = fullPath2id(conn, absPath)
    if -1 != did:
        return True,''
    
    stobj_path,abs_parent = conn.splitPath(absPath) 
    return insert_object(conn,'dir',stobj_path,abs_parent,'')

