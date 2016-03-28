# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.record import rdPut

def msgPut(db,path):

    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s PUT OBJECT %s' % (urName,objName)
    
    return rdPut(db, msg, urName, objPath)

def msgGet(db,path):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s DOWNLOAD OBJECT %s' % (urName,objName)
    
    return rdPut(db, msg, urName, objPath)

def msgHead(db,path):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s GET OBJECT %s INFO' % (urName,objName)
    
    return rdPut(db, msg, urName, objPath)

def msgMeta(db,path):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s GET OBJECT %s METADATA' % (urName,objName)
    
    return rdPut(db, msg, urName, objPath)

def msgDelete(db,path):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s DELETE OBJECT %s' % (urName,objName)
    
    return rdPut(db, msg, urName, objPath)

def msgDeleteRecycle(db,path):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s MOVE OBJECT %s TO RECYCLE' % (urName,objName)
    
    return rdPut(db, msg, urName, objPath)

def msgMove(db,path,dstName):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s MOVE OBJECT %s TO %s' % (urName,objName,dstName)
    
    return rdPut(db, msg, urName, objPath)

def msgCopy(db,path,dstName):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s COPY OBJECT %s TO %s'  % (urName,objName,dstName)
    
    return rdPut(db, msg, urName, objPath)

def msgMoveRecycle(db,path):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s MOVE OBJECT %s FROM RECYCLE' % (urName,objName)
    
    return rdPut(db, msg, urName, objPath)

def msgPost(db,path,header):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s UPDATE OBJECT METADATA %s' % (urName,objName,header)
    
    return rdPut(db, msg, urName, objPath)

