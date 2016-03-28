# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.record import rdPut

def msgDelete(db,path):
    pass

def msgPut(db,path):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s PUT ACCOUNT %s' % (urName,objName)
    
    return rdPut(db, msg, urName, objPath)
    
def msgHead(db,path):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s HEAD ACCOUNT %s'  % (urName,objName)
    return rdPut(db, msg, urName, objPath)
    
def msgGet(db,path):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' % GET ACCOUNT %s CONTENT' % (urName,objName)
    return rdPut(db, msg, urName, objPath)
    
def msgMeta(db,path):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' % GET ACCOUNT %s METADATA' % (urName,objName)
    return rdPut(db, msg, urName, objPath)
    
def msgPost(db,path,header):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s UPDATE ACCOUNT %s METADATA %s' % (urName,objName,header)
    return rdPut(db, msg, urName, objPath)

    