# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.table.user import getUsers,User,path2attr
from cloudweb.db.table.stobj import account2id

# urList -> user_list

def user_list(db):
    
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
            attr.update({'stid':account2id(db, data[1])})
            attr.update({'userid':data[0]})
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
        attr.update({'stid':account2id(db, data[1])})
        attr.update({'userid':data[0]})
        if str(data[2]) == u.typeAdmin:
            attr.update({u.type:'admin'})
        else:
            attr.update({u.type:'user'})
        attr.update({u.state:data[3]})
    return attr

    

