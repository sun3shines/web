# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.db_record import record_put

# msgDelete -> db_message_dir_delete
# msgReset -> db_message_dir_reset
# msgDeleteRecycle -> db_message_dir_deleterecycle
# msgMoveRecycle -> db_message_dir_moverecycle
# msgPut -> db_message_dir_put
# msgMove -> db_message_dir_move
# msgCopy -> db_message_dir_copy
# msgMetaGet -> db_message_dir_metaget
# msgGet -> db_message_dir_get

def db_message_dir_delete(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s DELETE DIR %s' % (urName,objName)
    
    return record_put(db, msg, urName, objPath)

def db_message_dir_reset(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s RESET DIR %s' % (urName,objName)
    
    return record_put(db, msg, urName, objPath)

def db_message_dir_deleterecycle(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s MOVE DIR %s TO RECYCLE' % (urName,objName)
    
    return record_put(db, msg, urName, objPath)

def db_message_dir_moverecycle(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s MOVE DIR %s FROM RECYCLE' % (urName,objName)
    
    return record_put(db, msg, urName, objPath)

def db_message_dir_put(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s PUT DIR %s' % (urName,objName)
    
    return record_put(db, msg, urName, objPath)

def db_message_dir_move(db,objPath,dstName):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s MOVE DIR %s TO %s' % (urName,objName,dstName)
    
    return record_put(db, msg, urName, objPath)

def db_message_dir_copy(db,objPath,dstName):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s COPY DIR %s TO %s' % (urName,objName,dstName)
    
    return record_put(db, msg, urName, objPath)

def db_message_dir_metaget(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s GET DIR %s INFO' % (urName,objName)
    
    return record_put(db, msg, urName, objPath)

def db_message_dir_get(db,objPath):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s GET DIR %s CONTENT' % (urName,objName)
    
    return record_put(db, msg, urName, objPath)
