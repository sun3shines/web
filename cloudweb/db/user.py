# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.table.user import userDisable,userEnable,userPut,getUsers,\
    User,path2attr
from cloudweb.db.table.mysql import getDb
def urPut(db,path):
    
    path = unquote(path)
    newPath = '/'.join(path.split('/')[3:])
    userPut(db, newPath)
    
def urDelete(db,userName):
    return userDisable(db, userName)

def urEnable(db,userName):
    return userEnable(db, userName)

def urDisable(db,userName):
    return userDisable(db, userName)

def urList(db):
    
    u = User()
    attrs = []
    datas = getUsers(db)
    if datas:
        for data in datas:
            attr = {}
            attr.update({u.id:data[0]})
            attr.update({u.name:data[1]})
            attr.update({u.type:data[2]})
            attr.update({u.state:data[3]})
            attrs.append(attr)
    return attrs

def user2attr(db,userName):
    attr = {}
    u = User()
    datas = path2attr(db, userName)
    if datas:
        data = datas[0]
        attr.update({u.id:data[0]})
        attr.update({u.name:data[1]})
        if str(data[2]) == u.typeAdmin:
            attr.update({u.type:'admin'})
        else:
            attr.update({u.type:'user'})
        attr.update({u.state:data[3]})
    return attr

if __name__ == '__main__':
    
    db = getDb()
      
    urPut(db,'/zhu__feng00000com/0/AUTH_zhu__feng00000com')
    # urDisable(db,'AUTH_zhu__feng00000com') 
    print urList(db)
    

