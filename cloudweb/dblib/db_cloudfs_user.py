# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.table.user import userPut
# from cloudweb.db.table.mysql import getDb
from cloudweb.db.db_user import user_list
# urPut -> db_cloudfs_user_put

def db_cloudfs_user_put(db,newPath):
    
    # path = unquote(path)
    # newPath = '/'.join(path.split('/')[3:])
    userPut(db, newPath)
    
if __name__ == '__main__':
    pass

    # db = getDb()
      
    # db_cloudfs_user_put(db,'/zhu__feng00000com/0/AUTH_zhu__feng00000com')
    # urDisable(db,'AUTH_zhu__feng00000com') 
    # print user_list(db)
    