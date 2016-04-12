# -*- coding: utf-8 -*-

import json
import cloudapi.missions.mission as mission
from cloudapi.missions.tasks.fs import AccountList,ContainerList,DirList
from cloudapi.missions.apis.user import user_login

def list_account(atName):
    '''
    功能：获取用户下的容器
    输入：用户名
    输出：path 名称
          state：忽略
          type:类型
          id:数据库id
          parent_id:父路径id
    '''
    t = AccountList(atName)
    t = mission.execute(t)
    
    print t.response
    return t.response

def list_container(atName,cntPath,tree=False):

    '''
    功能：获取容器下的对象
    输入：用户名，容器路径
    输出：path:对象路径
          state：对象状态
          type：对象类型
          id：对象数据库id
          parent_id:父路径id
    '''    
    t = ContainerList(atName,cntPath,tree)
    t = mission.execute(t)
    
    print t.response
    return t.response

def list_dir(atName,drPath,tree=False):
   
    '''
    功能：获取目录下的文件
    输入：用户名，目录路径
    输出：path:对象路径
          state：对象状态
          type：对象类型
          id：对象数据库id
          parent_id:父路径id
    ''' 
    t = DirList(atName,drPath,tree)
    t = mission.execute(t)
    
    print t.response
    return t.response
