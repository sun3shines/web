# -*- coding: utf-8 -*-

from urllib import unquote
import cloudmiddleware.mission as mission 
from cloudmiddleware.class_account import CloudAccountPut,CloudAccountDelete,CloudAccountValid

from cloudweb.db.account import atdelete,atput
from cloudweb.db.firewall import atValid
from cloudweb.db.user import urPut
from cloudweb.db.message.account import msgPut,msgDelete,msgHead,msgGet,msgMeta,msgPost

def cloudfs_account_put(request_path):
    
    path = unquote(request_path)
    newPath = '/'.join(path.split('/')[3:])
    
    t = CloudAccountPut(newPath)
    mission.execute(t)
    return t.response
    
def cloudfs_account_delete(request_path):

    path = unquote(request_path)
    newPath = '/'.join(path.split('/')[3:])
    
    t = CloudAccountDelete(newPath)
    mission.execute(t)
    return t.response

def cloudfs_account_exists(request_path):
    
#     path = unquote(request_path)
#     newPath = path.split('/')[2]
    # 函数有待商议，应该是处理url请求时，判断用户是否存在了。目前来看，没有依赖于数据库
    # 的可用性，此函数的意义已经不大了。
    pass

def cloudfs_account_get():
    pass

def cloudfs_account_post():
    pass

