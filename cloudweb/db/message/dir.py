# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.record import rdPut

def msgDelete(db,path):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s DELETE DIR %s' % (urName,objName)
    
    return rdPut(db, msg, urName, objPath)

def msgReset(db,path):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s RESET DIR %s' % (urName,objName)
    
    return rdPut(db, msg, urName, objPath)

def msgDeleteRecycle(db,path):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s MOVE DIR %s TO RECYCLE' % (urName,objName)
    
    return rdPut(db, msg, urName, objPath)

def msgMoveRecycle(db,path):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s MOVE DIR %s FROM RECYCLE' % (urName,objName)
    
    return rdPut(db, msg, urName, objPath)

def msgPut(db,path):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s PUT DIR %s' % (urName,objName)
    
    return rdPut(db, msg, urName, objPath)

def msgMove(db,path,dstName):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s MOVE DIR %s TO %s' % (urName,objName,dstName)
    
    return rdPut(db, msg, urName, objPath)

def msgCopy(db,path,dstName):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s COPY DIR %s TO %s' % (urName,objName,dstName)
    
    return rdPut(db, msg, urName, objPath)

def msgMetaGet(db,path):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s GET DIR %s INFO' % (urName,objName)
    
    return rdPut(db, msg, urName, objPath)

def msgGet(db,path):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s GET DIR %s CONTENT' % (urName,objName)
    
    return rdPut(db, msg, urName, objPath)
