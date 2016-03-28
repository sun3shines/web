# -*- coding: utf-8 -*-

import MySQLdb

class dbConn:

    def __init__(self,host,user,passwd,port,db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.db = db
        self.flag = False

    def connect(self):
        
        if not self.flag:
            self.connection = MySQLdb.connect(host=self.host,user=self.user,
                                              passwd=self.passwd,port=self.port,db=self.db) 
            self.flag = True

    def close(self):

        if self.flag:
            self.connection.close()
            self.flag = False

    def fetch_one_data(self,sqlStr):
        self.connect()
        cur = self.connection.cursor()
        cur.execute(sqlStr)
        data = cur.fetchone()
        cur.close()
        self.connection.commit()
        return data

    def fetch_all_data(self,sqlStr):

        self.connect()
        cur = self.connection.cursor()
        cur.execute(sqlStr)
        data = cur.fetchall()
        cur.close()
        self.connection.commit()
        return data
 
    def fetch_one_path_id(self,path,parent_id):

        sql = "select id from stobj where parent_id=%d and path='%s' " % (parent_id,path)
        data = self.fetch_one_data(sql) 
        if data:
            return data[0] 
        return -1

    def fetch_path_id(self,path,parent=False):

        # if parent is True,then path will be insert to db though not exists 
        level = 0
        id = -1
        for ph in path.split('/'):
            if not ph:
                continue
 
            if 0 == level:
                id = self.fetch_account_id(ph)
                level = level+1
                continue
            parent_id = id
            id = self.fetch_one_path_id(ph,parent_id)
            if -1 == id:
                if parent:
                    self.insert_stobj('dir',ph,parent_id,'') 
                    id = self.fetch_one_path_id(ph,parent_id)
                else:
                    break
            level = level + 1

        return id

    def fetch_account_id(self,path):

        sql = "select id from stobj where type='account' and path='%s' " % (path)
        data = self.fetch_one_data(sql)
        if data:
            return data[0]

        return -1

    def account_exists(self,path):

        if -1 != self.fetch_account_id(path):
            return True
        return False

    def insert_stobj(self,stobj_type,stobj_path,stobj_parent_id,stobj_state):

        keyStr = "type , path"
        valStr = "'%s' , '%s'"  % (stobj_type,stobj_path)
        if stobj_parent_id:
            keyStr = keyStr + ', parent_id'
            valStr = valStr + ", '%s'" % (stobj_parent_id)
        if stobj_state:
            keyStr = keyStr + ', state'
            valStr = valStr + ", '%s'" % (stobj_state)
        sql = "insert into stobj (%s) values (%s) " % (keyStr,valStr)
        
        self.execute_sql(sql)
        return True,''

    def execute_sql(self,sqlStr):

        # conn = MySQLdb.connect(host='192.168.36.3',user='root',passwd='111111',port=3306,db='cloudweb')
        self.connect()
        cur = self.connection.cursor()
        cur.execute(sqlStr)
        cur.close()
        self.connection.commit()
        # conn.close()

    def insert_account(self,stobj_path):

        return self.insert_stobj('account',stobj_path,'','enable')

    def insert_container(self,stobj_path,abs_parent):

        parent_id = self.fetch_account_id(abs_parent)
        if -1 == parent_id:
            return False,'fetch account id error'
        return self.insert_stobj('container',stobj_path,parent_id,'')

    def insert_object(self,stobj_type,stobj_path,abs_parent,stobj_state):

        parent_id = self.fetch_path_id(abs_parent,parent=True)
        if -1 == parent_id:
            return False,'fetch parent path id error'
        return self.insert_stobj(stobj_type,stobj_path,parent_id,stobj_state)

    def insert_dir(self,absPath):

        stobj_path,abs_parent = self.splitPath(absPath) 
        return self.insert_object('dir',stobj_path,abs_parent,'')

    def insert_link(self,absPath,stobj_state = 'enable'): 

        stobj_path,abs_parent = self.splitPath(absPath) 
        return self.insert_object('link',stobj_path,abs_parent,stobj_state)

    def insert_file(self,absPath,stobj_state = 'enable'):
    
        stobj_path,abs_parent = self.splitPath(absPath) 
        return self.insert_object('file',stobj_path,abs_parent,stobj_state)

    def splitPath(self,absPath):
    
        return absPath.split('/')[-1],'/'.join(absPath.split('/')[:-1])

    def delete_stobj(self,id):

        sql = 'delete from stobj where id=%s' % (str(id))
        self.execute_sql(sql)
        return True,''

    def delete_child_stobj(self,id):

        sql = 'delete from stobj where parent_id=%s' % (str(id))
        self.execute_sql(sql)
        return True,''

    def update_stobj(self,id,new_parent_id,path):

        sql = "update stobj set parent_id=%s,path='%s' where id=%s " % (str(new_parent_id),path,str(id))
        self.execute_sql(sql)
        return True,''

    def move_object(self,srcNewPath,dstNewPath):

        id = self.fetch_path_id(srcNewPath)

        absDstNewPath = '/'.join(dstNewPath.split('/')[:-1])
        dstPh = dstNewPath.split('/')[-1]
        new_parent_id = self.fetch_path_id(absDstNewPath,parent=True)

        return self.update_stobj(id,new_parent_id,dstPh)

    def copy_object(self,srcNewPath,dstNewPath):

        queueids = []
        attrs = self.fetch_path_attrs(fullPath = srcNewPath)      
        new_parent_id = self.fetch_path_id('/'.join(dstNewPath.split('/')[:-1]),parent=True) 
        newPath = dstNewPath.split('/')[-1]
        attrs['parent_id'] = new_parent_id
        attrs['path'] = newPath

        queueids.append(attrs)
        while len(queueids) >0:
            attrs = queueids.pop(0)
            self.insert_stobj(attrs['type'],attrs['path'],attrs['parent_id'],attrs['state'])
            new_parent_id = self.fetch_one_path_id(attrs['path'],attrs['parent_id'])
            cldattrs = self.fetch_childs_attrs(attrs['id'])
            for attrs in cldattrs:
                attrs['parent_id'] = new_parent_id
            queueids.extend(cldattrs) 
        return True,''

    def fetch_one_attrs(self,id):

        attrs = {}
        sql = "select * from stobj where id=%d " % (id)
        data = self.fetch_one_data(sql)
        if data:
            attrs['id'] = data[0]
            attrs['path'] = data[1]
            attrs['type'] = data[2]
            attrs['parent_id'] = data[3]
            attrs['state'] = data[4]
            return attrs
        return attrs

    def fetch_path_attrs(self,fullPath):

        id = self.fetch_path_id(fullPath,parent=False) 
        attrs = self.fetch_one_attrs(id)
        return attrs

    def fetch_childs_attrs(self,parent_id):
        cldsattrs = []
        sql = "select * from stobj where parent_id=%d " % (parent_id)
        datas = self.fetch_all_data(sql)
        if datas:
            for data in datas:
                attrs = {}
                attrs['id'] = data[0]
                attrs['path'] = data[1]
                attrs['type'] = data[2]
                attrs['parent_id'] = data[3]
                attrs['state'] = data[4]
                cldsattrs.append(attrs)
            return cldsattrs

        return cldsattrs

    def search_global_objects(self,keyword):
        
        objects = []
        sql = "select * from stobj where path like'%" + keyword + "%'" 
        datas = self.fetch_all_data(sql)
        if datas:
            for data in datas:
                object = {}
                object['id'] = data[0]
                object['path'] = data[1]
                object['type'] = data[2]
                object['parent_id'] = data[3]
                object['state'] = data[4]
                objects.append(object)
            return objects

        return objects

    def search_account_objects(self,atName,keyWord):

        objects = []
        queueids = []
        attrs = self.fetch_path_attrs(fullPath = atName)
        queueids.append(attrs)

        while len(queueids) >0:
            attrs = queueids.pop(0)

            if attrs['path'].find(keyWord) != -1:
                objects.append(attrs)

            cldattrs = self.fetch_childs_attrs(attrs['id'])
            queueids.extend(cldattrs)
         
        return objects

def getDb():

    return dbConn('192.168.36.3','root','111111',3306,'cloudweb')

if __name__ == '__main__':

    conn = dbConn('192.168.36.3','root','111111',3306,'cloudweb')

#    conn.insert_account('a')
#    conn.insert_container('b','a')
#    conn.insert_dir('a/b/c') 
#    conn.insert_dir('a/b/目 录1/目 录5/目 录3')
#    conn.insert_dir('a/b/目 录1/目 录5/目 录4')
#    conn.insert_file('a/b/c/e')
#    conn.insert_link('a/b/c/f')    
#    conn.fetch_account_id('a')

#    conn.insert_account('用 户')
#    conn.insert_container('容 器','用 户')
#    conn.move_object('a/b/c','a/b/e/z')
#    conn.move_object('a/b','a/f')
#    print conn.fetch_path_attrs('a/f')
#    print conn.fetch_childs_attrs(1041)
#    conn.copy_object('AUTH_zhu__feng00000com/normal/目 录1/目 录5','AUTH_zhu__feng00000com/normal/testdir')
#    print conn.search_global_objects('目 录')
    print conn.search_account_objects('AUTH_zhu__feng00000com','目 录')
    print conn.search_account_objects('a','目 录')
    conn.close()


