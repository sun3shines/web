# -*- coding: utf-8 -*-

import json

from cloudweb.db.table.mysql import dbConn
from cloudweb.db.db_dir import insert_dir
from cloudweb.db.db_account import insert_account
from cloudweb.db.db_container import insert_container
from cloudweb.db.db_link import insert_link
from cloudweb.db.db_object import insert_file

from cloudweb.globalx.static import MYSQL_HOST,MYSQL_PORT,MYSQL_USER,MYSQL_PASSWD
from cloudlib.restful.cloudfs.lib_token import libGetToken
from cloudweb.drive.utils import getAtNameByEmail
from cloudlib.restful.cloudfs.lib_container import libGetContainerList
from cloudlib.restful.cloudfs.lib_object import libGetObjectList

class DbType:
    def __init__(self):
        self.account = 'account'
        self.container = 'container'
        self.object = 'object'
        self.dir = 'dir'
        self.file = 'file'
        self.link = 'link'
        
def insert_db_data(conn,objtype,dbpath):

    dt = DbType()
    
    newPath = dbpath
    if dt.account == objtype:
        accountPath = newPath 
        return insert_account(conn,accountPath)

    elif dt.container == objtype:
        aPath = newPath.split('/')[0]
        cPath = newPath.split('/')[-1]
        return insert_container(conn,cPath,aPath)
    elif dt.file == objtype:
        return insert_file(conn,newPath) 
    elif dt.link == objtype:
        return insert_link(conn,newPath)
    elif dt.dir == objtype:
        return insert_dir(conn,newPath)
    else:
        return False,'data type error'
    return True,''

def getDirList(conn,dbpath,level,filelist=[]):

    dt = DbType()
    if 0== level:
        stobj_type = dt.account
    elif 1== level:
        stobj_type = dt.container
    else:
        stobj_type = dt.dir

    insert_db_data(conn,stobj_type,dbpath)
    
    libobjlist = []
    if dt.account == stobj_type:
        resp = libGetContainerList(atName, token)
        libobjlist = resp.get('msg',[])
        
    elif dt.container == stobj_type:
        lib_container_path = '/'.join(['']+dbpath.split('/')[1:])
        resp = libGetObjectList(atName, token,lib_container_path)
        libobjlist = resp.get('msg',[])
        
    elif dt.dir == stobj_type:
        libobjlist = filelist
                
    for obj in libobjlist:
        objname = obj.get('name').encode('utf-8')
        dbobjpath = '/'.join([dbpath,objname])
        objtype = obj.get('ftype')
        
        if 'f' == objtype:
            insert_db_data(conn,'file',dbobjpath)
        elif 'l' == objtype:
            insert_db_data(conn,'link',dbobjpath) 
        else:
            getDirList(conn,dbobjpath,level+1,obj.get('list')) 
        
    return True,''

if __name__ == '__main__':
    
    import pdb;pdb.set_trace() 
    conn = dbConn(MYSQL_HOST,MYSQL_USER,MYSQL_PASSWD,MYSQL_PORT,'cloudweb') 
    
    email = 'testadministrator@163com'
    passwd = '123456'
    
    token = libGetToken(email, passwd)
    atName = getAtNameByEmail(email)
    
    getDirList(conn,atName,0)
    conn.close()
    
