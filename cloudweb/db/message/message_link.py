# -*- coding: utf-8 -*-

from urllib import unquote
from cloudweb.db.db_record import record_put

# msgPut -> db_message_link_put

def db_message_link_put(db,objPath,dstName):
    
    # objPath = unquote(path)
    # objPath = '/'.join(objPath.split('/')[3:])
    
    urName = objPath.split('/')[0]
    objName = objPath.split('/')[-1]
    
    msg = ' %s PUT LINK %s FROM %s' % (urName,dstName,objName)
    
    return record_put(db, msg, urName, objPath)
