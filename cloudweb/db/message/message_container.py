# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.db_record import record_put

# msgDelete -> db_message_container_delete
# msgPut -> db_message_container_put
# msgHead -> db_message_container_head
# msgMeta -> db_message_container_meta
# msgGet -> db_message_container_get
# msgPost -> db_message_container_post

def db_message_container_delete(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s DELETE CONTAINER %s' % (urName,objName)
    
    return record_put(db, msg, urName, objPath)

def db_message_container_put(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s PUT CONTAINER %s' % (urName,objName)
    
    return record_put(db, msg, urName, objPath)

def db_message_container_head(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s HEAD CONTAINER %s' % (urName,objName)
    
    return record_put(db, msg, urName, objPath)

def db_message_container_meta(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s GET CONTAINER %s METADATA' % (urName,objName)
    
    return record_put(db, msg, urName, objPath)

def db_message_container_get(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s GET CONTAINER %s CONTENT' % (urName,objName)
    
    return record_put(db, msg, urName, objPath)

def db_message_container_post(db,objPath,header):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s UPDATE CONTAINER %s METADATA %s' % (urName,objName,header)
    
    return record_put(db, msg, urName, objPath)

