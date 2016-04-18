# -*- coding: utf-8 -*-

import json
from cloudlib.common.bufferedhttp import jresponse

from cloudweb.dblib.db_flask_account import db_flask_account_list
from cloudweb.dblib.db_flask_container import db_flask_container_list
from cloudweb.dblib.db_flask_dir import db_flask_dir_list
from cloudweb.globalx.variable import GLOBAL_USER_DB
def flasklistAccount(req,sdata):
    param = json.loads(req.body)
    atName = param.get('atName')
    conn = GLOBAL_USER_DB.get(atName)
    metadata = db_flask_account_list(conn,atName)
    
    return jresponse('0',json.dumps(metadata),req,200)

def flasklistContainer(req,sdata):
    param = json.loads(req.body)
    atName = param.get('atName')
    cntPath = param.get('cntPath')
    tree = param.get('tree')
    
    conn = GLOBAL_USER_DB.get(atName)
    metadata = db_flask_container_list(conn, atName, cntPath,tree)
    return jresponse('0',json.dumps(metadata),req,200)

def flasklistDir(req,sdata):
    
    param = json.loads(req.body)
    atName = param.get('atName')
    drPath = param.get('drPath')
    tree = param.get('tree')
    
    conn = GLOBAL_USER_DB.get(atName)
    metadata = db_flask_dir_list(conn,atName,drPath,tree)
    return jresponse('0',json.dumps(metadata),req,200)

