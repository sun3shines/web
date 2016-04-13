# -*- coding: utf-8 -*-

from cloudweb.db.db_link import insert_link

# lkput -> db_cloudfs_link_put

def db_cloudfs_link_put(newPath,conn):
    
    # path = unquote(path)
    # newPath = '/'.join(path.split('/')[3:])
    return insert_link(conn,newPath)