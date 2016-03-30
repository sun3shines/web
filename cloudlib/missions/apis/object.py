# -*- coding: utf-8 -*-

import cloudlib.missions.mission as mission
from cloudlib.missions.tasks.object import *
from cloudlib.missions.apis.user import user_login

def disable_object(atName,objPath):
    '''
    功能：禁用文件
    输入：用户名，对象路径
    输出: 无
    '''    
    t = ObjectDisable(atName,objPath)
    mission.execute(t)
    print t.response
    return t.response

def enable_object(atName,objPath):
    '''
    功能：启用文件
    输入：用户名，对象路径
    输出：无
    ''' 
    t = ObjectEnable(atName,objPath)
    mission.execute(t)
    print t.response
    return t.response

def delete_object(atName,objPath):
    '''
    功能：删除文件
    输入：用户名，对象路径
    输出：无
    ''' 
    t = ObjectDelete(atName,objPath)
    mission.execute(t)
    print t.response
    return t.response

def download_object(atName,objPath):
    '''
    功能：下载文件
    输入：用户名，对象路径
    输出：文件数据
    '''    
    t = ObjectDownload(atName,objPath)
    app_iter = mission.download(t)
    return app_iter

def upload_object(atName,dst,localPath):
    '''
    功能：上传文件
    输入：用户名，目标路径，源文件路径
    输出：ctime：创建时间
          mtime：修改时间
          permission：文件权限
          path：路径
          md5：文件md5
          size：文件大小
    '''
    t = ObjectUpload(atName,dst,localPath)
    mission.execute(t)
    print t.response
    return t.response

