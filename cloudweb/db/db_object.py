# -*- coding: utf-8 -*-

from cloudweb.db.table.stobj import insert_object
 
def insert_file(conn,absPath,stobj_state = 'enable'):

    stobj_path,abs_parent = conn.splitPath(absPath) 
    return insert_object(conn,'file',stobj_path,abs_parent,stobj_state)
