# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.db_record import record_put

# msgDelete -> db_message_account_delete
# msgPut -> db_message_account_put
# msgHead -> db_message_account_head
# msgGet -> db_message_account_get
# msgMeta -> db_message_account_meta
# msgPost -> db_message_account_post

def db_message_account_delete(db,path):
    pass

def db_message_account_put(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s PUT ACCOUNT %s' % (urName,objName)
    
    return record_put(db, msg, urName, objPath)
    
def db_message_account_head(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s HEAD ACCOUNT %s'  % (urName,objName)
    return record_put(db, msg, urName, objPath)
    
def db_message_account_get(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' % GET ACCOUNT %s CONTENT' % (urName,objName)
    return record_put(db, msg, urName, objPath)
    
def db_message_account_meta(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' % GET ACCOUNT %s METADATA' % (urName,objName)
    return record_put(db, msg, urName, objPath)
    
def db_message_account_post(db,objPath,header):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s UPDATE ACCOUNT %s METADATA %s' % (urName,objName,header)
    return record_put(db, msg, urName, objPath)

    