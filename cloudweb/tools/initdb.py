# -*- coding: utf-8 -*-

import os.path
import os

from cloudweb.db.table.mysql import dbConn
from cloudweb.db.db_dir import insert_dir
from cloudweb.db.db_account import insert_account
from cloudweb.db.db_container import insert_container
from cloudweb.db.db_link import insert_link
from cloudweb.db.db_object import insert_file

from cloudweb.globalx.static import MYSQL_HOST,MYSQL_PORT,MYSQL_USER,MYSQL_PASSWD

class fsDataDb:

    def __init__(self,conn):
        self.conn = conn

    def insert_db_data(self,type,path):
    
        newPath = '/'.join(path.split('/')[3:])
        if 'account' == type:
            accountPath = newPath 
            return insert_account(self.conn,accountPath)

        elif 'container' == type:
            aPath = newPath.split('/')[0]
            cPath = newPath.split('/')[-1]
            return insert_container(self.conn,cPath,aPath)
        elif 'file' == type:
            return insert_file(self.conn,newPath) 
        elif 'link' == type:
            return insert_link(self.conn,newPath)
        elif 'dir' == type:
            return insert_dir(self.conn,newPath)
        else:
            return False,'data type error'
        return True,''

    ## get file or link type

    def getObjData(self,path,level):

        stobj_path = path.split('/')[-1]
        stobj_type = 'object'
        if os.path.isfile(path):
            stobj_type = 'file'
        elif os.path.islink(path):
            stobj_type = 'link'
        else:
            stobj_type = 'object'

        print stobj_type,stobj_path
        flag,msg = self.insert_db_data(stobj_type,path)
        if not flag:
            return False,msg

        return True,''


    ## get dir data and type
    def getDirList(self,path,level):

        if not os.path.isdir(path):
            return False,'path not dir'

        stobj_path = path.split('/')[-1]

        if 0== level:
            stobj_type = 'account'
        elif 1== level:
            stobj_type = 'container'
        else:
            stobj_type = 'dir'

        print stobj_type,stobj_path
        flag,msg = self.insert_db_data(stobj_type,path)
        if not flag:
            return False,msg

        if not os.path.exists(path):
            return False,'dir not exists'

        objlist = os.listdir(path)
        for obj in objlist:
            objpath = '/'.join([path,obj])
            if os.path.isdir(objpath):
                if 'ff89f933b2ca8df40' == obj:
                    continue
                flag,msg = self.getDirList(objpath,level+1) 
            else:
                flag,msg = self.getObjData(objpath,level+1) 

            if not flag:
                print msg
            
        return True,''

    def getFsData(self,storage_device):
 
        objlist = os.listdir(storage_device)
        for obj in objlist:
            objpath = '/'.join([storage_device,obj])
            if not os.path.isdir(objpath):
                continue
            if 'ff89f933b2ca8df40' == obj:
                continue
            flag,msg = self.getDirList(objpath,0)
            if not flag:
                print msg

    def close(self):
        self.conn.close()

if __name__ == '__main__':
    
    conn = dbConn(MYSQL_HOST,MYSQL_USER,MYSQL_PASSWD,MYSQL_PORT,'cloudweb') 
    fsobj = fsDataDb(conn)
    fsobj.getFsData('/mnt/cloudfs-object')
    fsobj.close()

