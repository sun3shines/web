# -*- coding: utf-8 -*-

import json
from cloudcommon.common.bufferedhttp import jresponse
from cloudweb.db.account import atList
from cloudweb.db.container import cntList
from cloudweb.db.dir import drList

def listAccount(req,sdata):
    param = json.loads(req.body)
    atName = param.get('atName')
    ev = sdata.user.getUser(atName)
    metadata = atList(ev.db,atName)
    
    return jresponse('0',json.dumps(metadata),req,200)

def listContainer(req,sdata):
    param = json.loads(req.body)
    atName = param.get('atName')
    cntPath = param.get('cntPath')
    tree = param.get('tree')
    ev = sdata.user.getUser(atName)
    
    metadata = cntList(ev.db, atName, cntPath,tree)
    return jresponse('0',json.dumps(metadata),req,200)

def listDir(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    drPath = param.get('drPath')
    tree = param.get('tree')
    ev = sdata.user.getUser(atName)
    metadata = drList(ev.db,atName,drPath,tree)
    return jresponse('0',json.dumps(metadata),req,200)
