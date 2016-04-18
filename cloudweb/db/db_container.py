# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.table.stobj import account2id,insert_stobj,fullPath2id

def insert_container(conn,stobj_path,abs_parent):

    did = fullPath2id(conn, '/'.join([abs_parent,stobj_path]))
    if -1 != did:
        return True,''

    parent_id = account2id(conn,abs_parent)
    if -1 == parent_id:
        return False,'fetch account id error'
    
    return insert_stobj(conn,'container',stobj_path,parent_id,'')


