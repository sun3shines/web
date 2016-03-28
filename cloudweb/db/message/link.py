# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.record import rdPut

def msgPut(db,path,dstName):
    
    objPath = unquote(path)
    objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s PUT LINK %s FROM %s' % (urName,dstName,objName)
    
    return rdPut(db, msg, urName, objPath)
