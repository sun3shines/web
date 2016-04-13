# -*- coding: utf-8 -*-

from cloudweb.db.table.stobj import insert_object

def insert_dir(conn,absPath):

    stobj_path,abs_parent = conn.splitPath(absPath) 
    return insert_object(conn,'dir',stobj_path,abs_parent,'')

