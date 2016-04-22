# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse
from cloudweb.dblib.db_cloudfs_link import db_cloudfs_link_put
from cloudweb.db.message.message_link import db_message_link_put
from cloudweb.platform.globalx.variable import GLOBAL_USER_DB 
from cloudweb.platform.drive.consistency import db_consistent
from cloudweb.db.table.lock.mysql import getlock

@db_consistent
def cloudfsLinkPut(req):
    
    param = json.loads(req.body)
    newPath = param.get('newPath')
    
    objPath = param.get('objPath')
    dstName = param.get('dstName')
    
    atName = newPath.split('/')[0]
    conn = GLOBAL_USER_DB.get(atName)
    with getlock(conn) as mylock:
        db_cloudfs_link_put(newPath, conn)
        db_message_link_put(conn, objPath, dstName)
    
    return jresponse('0','',req,200)

