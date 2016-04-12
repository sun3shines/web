# -*- coding: utf-8 -*-

import cloudapi.missions.mission as mission
from cloudapi.missions.tasks.record import AccountRecord,ObjectRecord
from cloudapi.missions.apis.user import user_login

def get_account_records(atName,start=0,num=0):
    '''
    功能：获取用户操作记录
    输入：用户名
    输出：数据库id，消息正文，时间
    '''    
    t = AccountRecord(atName )
    t = mission.execute(t)
    print t.response
    return t.response

def get_object_records(atName,objPath,start=0,num=0):
    '''
    功能：获取对象操作记录
    输入：用户名，对象路径
    输出：数据库id，消息正文，时间
    ''' 
    t = ObjectRecord(atName,objPath )
    t = mission.execute(t) 
    print t.response
    return t.response

