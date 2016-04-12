# -*- coding: utf-8 -*-

import cloudapi.missions.mission as mission

from cloudapi.missions.tasks.search import *
from cloudapi.missions.apis.user import user_login

def data_user_find(atName,keyword):
    '''
    功能：根据关键字搜索用户空间内的对象
    输入：用户名，关键字
    输出：path:路径
          state:状态
          type:类型
          id:数据库id 
          parent_id:父路径id
    ''' 
    t = UserSearch(atName,keyword)
    mission.execute(t)
    print t.response
    return t.response

def data_global_find(atName,keyword):
   
    '''
    功能：根据关键字搜索全局空间内的对象
    输入：管理员用户名，关键字
    输出：path:路径
          state:状态
          type:类型
          id:数据库id 
          parent_id:父路径id
    '''
 
    t = GlobalSearch(atName,keyword)
    mission.execute(t)
    print t.response
    return t.response

def data_md5_find(atName,keyword):
    t = Md5Search(atName,keyword)
    mission.execute(t)
    print t.response
    return t.response

def get_object_details(atName,objectId):
    '''
    功能：获取对象详细信息
    输入：用户名，对象数据库id
    输出：urlpath 对象全路径
    账户：Account-Bytes-Used 账户已用空间，Account-Meta-Quota-Bytes 账户配额
    容器：container-bytes-used 容器已用空间，versions-location 容器版本容器，container-object-count 容器对象数量
    对象：object-permisson 权限，content-length 文件大小，file-type 对象类型,md5 文件md5值
    '''
    t = ObjectDetails(atName,objectId)
    mission.execute(t)
    print t.response
    return t.response


