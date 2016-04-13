# -*- coding: utf-8 -*-

from cloudweb.db.table.stobj import insert_object

def insert_link(conn,absPath,stobj_state = 'enable'): 

    stobj_path,abs_parent = conn.splitPath(absPath) 
    return insert_object(conn,'link',stobj_path,abs_parent,stobj_state)


    
