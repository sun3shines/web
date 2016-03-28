# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.record import rdPut

def msgDelete(db,path):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s DELETE CONTAINER %s' % (urName,objName)
    
    return rdPut(db, msg, urName, objPath)

def msgPut(db,path):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s PUT CONTAINER %s' % (urName,objName)
    
    return rdPut(db, msg, urName, objPath)

def msgHead(db,path):
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s HEAD CONTAINER %s' % (urName,objName)
    
    return rdPut(db, msg, urName, objPath)

def msgMeta(db,path):
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s GET CONTAINER %s METADATA' % (urName,objName)
    
    return rdPut(db, msg, urName, objPath)

def msgGet(db,path):
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s GET CONTAINER %s CONTENT' % (urName,objName)
    
    return rdPut(db, msg, urName, objPath)

def msgPost(db,path,header):
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s UPDATE CONTAINER %s METADATA %s' % (urName,objName,header)
    
    return rdPut(db, msg, urName, objPath)

