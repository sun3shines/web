# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.db_record import record_put

# msgPut -> db_message_object_put
# msgGet -> db_message_object_get
# msgHead -> db_message_object_head
# msgMeta -> db_message_object_meta
# msgDelete -> db_message_object_delete
# msgDeleteRecycle -> db_message_object_deleterecycle
# msgMove -> db_message_object_move
# msgCopy -> db_message_object_copy
# msgMoveRecycle -> db_message_object_moverecycle
# msgPost -> db_message_object_post

def db_message_object_put(db,objPath):

#    objPath = unquote(path)
#    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s PUT OBJECT %s' % (urName,objName)
    
    return record_put(db, msg, urName, objPath)

def db_message_object_get(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s DOWNLOAD OBJECT %s' % (urName,objName)
    
    return record_put(db, msg, urName, objPath)

def db_message_object_head(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s GET OBJECT %s INFO' % (urName,objName)
    
    return record_put(db, msg, urName, objPath)

def db_message_object_meta(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s GET OBJECT %s METADATA' % (urName,objName)
    
    return record_put(db, msg, urName, objPath)

def db_message_object_delete(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s DELETE OBJECT %s' % (urName,objName)
    
    return record_put(db, msg, urName, objPath)

def db_message_object_deleterecycle(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s MOVE OBJECT %s TO RECYCLE' % (urName,objName)
    
    return record_put(db, msg, urName, objPath)

def db_message_object_move(db,objPath,dstName):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s MOVE OBJECT %s TO %s' % (urName,objName,dstName)
    
    return record_put(db, msg, urName, objPath)

def db_message_object_copy(db,objPath,dstName):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s COPY OBJECT %s TO %s'  % (urName,objName,dstName)
    
    return record_put(db, msg, urName, objPath)

def db_message_object_moverecycle(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s MOVE OBJECT %s FROM RECYCLE' % (urName,objName)
    
    return record_put(db, msg, urName, objPath)

def db_message_object_post(db,objPath,header):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s UPDATE OBJECT METADATA %s' % (urName,objName,header)
    
    return record_put(db, msg, urName, objPath)

