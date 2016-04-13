# -*- coding: utf-8 -*-

from cloudweb.db.table.stobj import account2id,insert_stobj

def account_exists(conn,path):

    if -1 != account2id(conn,path):
        return True
    return False

def insert_account(conn,stobj_path):

    return insert_stobj(conn,'account',stobj_path,'','enable')

