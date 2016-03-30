# -*- coding: utf-8 -*-

import cloudlib.missions.mission as mission
from cloudlib.missions.tasks.quota import QuotaGet,QuotaSet
from cloudlib.missions.apis.user import user_login

def get_account_quota(atName):
    '''
    功能：获取用户配额信息
    输入：用户名
    输出：bytes-used：空间已使用字节数
          quota-bytes:用户配额大小
    '''    
    t = QuotaGet(atName)
    mission.execute(t)
    print t.response
    return t.response
    
def set_account_quota(atName,val ):
    '''
    功能：设置用户配额值
    输入：用户名，配额字节数（1G则val为1024*1024*1024）
    输出：无
    ''' 
    t = QuotaSet(atName,val)
    mission.execute(t)
    print t.response
    return t.response
