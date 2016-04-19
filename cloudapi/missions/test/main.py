

from cloudapi.missions.apis.fs import list_account,list_container,list_dir
from cloudapi.missions.apis.object import disable_object,enable_object,delete_object,\
    download_object,upload_object
from cloudapi.missions.apis.quota import get_account_quota,set_account_quota
from cloudapi.missions.apis.record import get_account_records,get_object_records
from cloudapi.missions.apis.search import data_global_find,data_user_find,data_md5_find,\
    get_object_details
from cloudapi.missions.apis.user import user_login,get_accounts,disable_account,\
    enable_account,delete_account
    
def fs_test(atName):
    list_account(atName)
    list_container(atName,'/normal')
    list_dir(atName,'/normal/dir')
    
def object_test(atName):
    
    upload_object(atName,'/normal/test3.txt','/root/install.log')
    app_iter = download_object(atName,'/normal/test.txt')
    for data in app_iter:
        print data
    disable_object(atName,'/normal/test.txt')
    enable_object(atName,'/normal/test.txt')   
    delete_object(atName,'/normal/test3.txt')

def quota_test(atName):

    get_account_quota(atName)
    set_account_quota(atName,str(1024*1024*1024))
    get_account_quota(atName)

def record_test(atName):

    get_account_records(atName)
    get_object_records(atName,'/normal/dir')

def search_test(atName):
    data_user_find(atName,'normal')    
    get_object_details(atName,'1340')
    data_user_find(atName,'zhu__feng')
    get_object_details(atName,'1339')
    data_user_find(atName,'test')
    get_object_details(atName,'1350')
def user_test(atName):
    
    disable_account(atName,atName) 
    enable_account(atName,atName)
    get_accounts(atName)
    delete_account(atName,atName)

if __name__ == '__main__': 

    email = 'zhu__feng001@163com'
    passwd = '123456'
    atName = 'AUTH_zhu__feng001163com'
    user_login(email,passwd)
    
#    fs_test(atName)
#    object_test(atName)    
#    quota_test(atName)
#    record_test(atName)
#    search_test(atName)
    user_test(atName)

