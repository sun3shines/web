# -*- coding: utf-8 -*-

import cloudweb.missions.mission as mission
from cloudweb.missions.tasks.user import UserLogin, UserList, UserDisable, \
    UserEnable,UserDelete

def user_login(email,passwd):
    ''' 
    功能：用户登录
    输入：用户邮箱，密码
    输出：access_token:用户token
          expires：超时时间
          tanent：账户名
          name:数据库用户名
          state：账户状态
          type：用户类型
          id：数据库id
    备注：tanent不可直接使用，作为atName参数使用时，使用name值
    '''    
    t = UserLogin(email,passwd)
    mission.execute(t)
    print t.response
    return t.response

def get_accounts(atName,start=0,num=0):
    '''
    功能：获取账户信息
    输入：管理员账户
    输出：state 账户状态
          type 账户类型
          name：账户名
    ''' 
    t = UserList(atName)
    mission.execute(t)
    print t.response
    return t.response
def disable_account(atName,urName):
    '''
    功能：禁用账户
    输入：管理员账户，被禁用账户名
    输出：无
    '''
    t = UserDisable(atName,urName)
    mission.execute(t)
    print t.response
    return t.response


def enable_account(atName,urName):
    '''
    功能：启用账户
    输入：管理员账户，被启用账户名
    输出：无
    '''
    t = UserEnable(atName,urName)
    mission.execute(t)
    print t.response
    return t.response

def delete_account(atName,urName):
    '''
    功能：删除账户
    输入：管理员账户，被删除账户名
    输出：无
    备注：实际并未删除，禁用账户，可通过启动恢复
    '''
    t = UserDelete(atName,urName)
    mission.execute(t)
    print t.response
    return t.response

