# -*- coding: utf-8 -*-

from urllib import unquote

from cloudweb.db.table.mysql import getDb
from cloudweb.db.table.stobj import fullPath2attrs

def otValid(path,db):
    ## 不可在__call__ 函数中调用，因为对于put函数无效了。    
    path = unquote(path)
    newPath = '/'.join(path.split('/')[3:])

    attr = fullPath2attrs(db,newPath)
    if 'disable'  != attr.get('state'):
        return True 
    
    return False

def atValid(path,db):
    
    path = unquote(path)
    newPath = '/'.join(path.split('/')[3:])
    
    attr = fullPath2attrs(db,newPath)
    if 'disable'  != attr.get('state'):
        return True
    
    return False

if __name__ == "__main__":

    db = getDb()
    # atPath = '/zhu__feng001163com/0/AUTH_zhu__feng001163com' 
    # print atValid(atPath,db)

    otPath = '/zhu__feng001163com/0/AUTH_zhu__feng001163com/normal/test.txt'
    print otValid(otPath,db)



