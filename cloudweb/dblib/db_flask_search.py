# -*- coding: utf-8 -*-

from cloudweb.db.db_search import search_account_objects,search_global_objects

def db_flask_search_global_objects(conn,keyword):
    return search_global_objects(conn,keyword)

def db_flask_search_account_objects(conn,atName,keyWord):
    return search_account_objects(conn,atName,keyWord)