# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.table.stobj import account2id,insert_stobj

def insert_container(conn,stobj_path,abs_parent):

    parent_id = account2id(conn,abs_parent)
    if -1 == parent_id:
        return False,'fetch account id error'
    return insert_stobj(conn,'container',stobj_path,parent_id,'')


