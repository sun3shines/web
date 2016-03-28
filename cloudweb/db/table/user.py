# -*- coding: utf-8 -*-

from urllib import unquote

class User:
    def __init__(self):
        
        self.table = 'user'
        self.id = 'id'
        self.name = 'name'
        self.type = 'type' # 1为普通用户，0为管理用户
        self.state = 'state'
        self.email = 'email'
        self.password = 'password'
        
        self.typeUser = '1'
        self.typeAdmin = '0'
    
def addUser(db):
    
    return True,''


def insert_user(db,userName,userType,userState,userEmail='',userPasswd=''):
    
    u = User()
    keys = [u.name,u.type,u.state]
    vals = [userName,userType,userState]
    
    if userEmail:
        keys.append(u.email)
        vals.append(userEmail)
    if userPasswd:
        keys.append(u.password)
        vals.append(userPasswd)
        
    return db.insert(keys,vals,u.table)
    
def name2id(db,userName):
    
    u = User()
    attrs = [u.id]
    c = {u.name:userName}
    
    data = db.select(attrs,u.table,c)
    if data:
        return data[0][0]
    return -1

def update_user(db,userName,admin=False,userState='',userPasswd=''):
    
    u = User()
    c = {u.name:userName}
    s = {}
    if admin:
        s.update({u.type:u.typeAdmin})
    if userState:
        s.update({u.state:userState})
    if userPasswd:
        s.update({u.password:userPasswd})
    return db.update(s,u.table,c)


def userEnable(db,userName):
    
    return update_user(db,userName,userState='enable')

def userDisable(db,userName):
    
    return update_user(db,userName,userState='disable')

def userPut(db,userName):
    
    u = User()
    return insert_user(db,userName,userType=u.typeUser,userState='enable',userEmail=userName)

def getUsers(db):
    
    u = User()
    return db.select([u.id,u.name,u.type,u.state],u.table)

def path2attr(db,userName):
    u = User()
    
    return db.select([u.id,u.name,u.type,u.state],u.table,{u.name:userName})


