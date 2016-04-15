# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse

from cloudweb.dblib.db_flask_account import db_flask_account_list
from cloudweb.dblib.db_flask_container import db_flask_container_list
from cloudweb.dblib.db_flask_dir import db_flask_dir_list

def flasklistAccount(req,sdata):
    param = json.loads(req.body)
    atName = param.get('atName')
    ev = sdata.user.getUser(atName)
    metadata = db_flask_account_list(ev.db,atName)
    
    return jresponse('0',json.dumps(metadata),req,200)

def flasklistContainer(req,sdata):
    param = json.loads(req.body)
    atName = param.get('atName')
    cntPath = param.get('cntPath')
    tree = param.get('tree')
    ev = sdata.user.getUser(atName)
    
    metadata = db_flask_container_list(ev.db, atName, cntPath,tree)
    return jresponse('0',json.dumps(metadata),req,200)

def flasklistDir(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    drPath = param.get('drPath')
    tree = param.get('tree')
    ev = sdata.user.getUser(atName)
    metadata = db_flask_dir_list(ev.db,atName,drPath,tree)
    return jresponse('0',json.dumps(metadata),req,200)

