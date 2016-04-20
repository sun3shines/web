# -*- coding: utf-8 -*-

from cloudlib.common.exceptions import LockTimeout, MessageTimeout
from cloudlib.urls.flask import *

from cloudweb.platform.http_flask_fs import flasklistAccount,flasklistContainer,flasklistDir
from cloudweb.platform.http_flask_user import flaskUserDelete,flaskUserDisable,flaskUserEnable,flaskUserList,flaskUserLogin
from cloudweb.platform.http_flask_search import flaskDataGlobalSearch,flaskDataObjectDetail,flaskDataUserSearch
from cloudweb.platform.http_flask_object import flaskDeleteObject,flaskDisableObject,flaskDownloadObject,flaskEnableObject,flaskUploadObject
from cloudweb.platform.http_flask_quota import flaskQuotaGet,flaskQuotaSet
from cloudweb.platform.http_flask_record import flaskGetAccountRecords,flaskGetObjectRecords
from cloudweb.platform.http_flask_host import flaskQueryAllStatic,flaskQueryService,flaskQueryStatClass
def flaskUrl2View():
    url2view = {}
    url2view.update({strUserLogin:flaskUserLogin}) # restful
    url2view.update({strUserList:flaskUserList})
    url2view.update({strUserEnable:flaskUserEnable})
    url2view.update({strUserDisable:flaskUserDisable})
    url2view.update({strUserDelete:flaskUserDelete})
    
    url2view.update({strGetServiceStatus:flaskQueryService})
    url2view.update({strGetWorkloadStatus:flaskQueryStatClass})
    url2view.update({strGetHostStatic:flaskQueryAllStatic})
    url2view.update({strGetAbnormalEvents:None})
    
    url2view.update({strDataGlobalSearch:flaskDataGlobalSearch})
    url2view.update({strDataUserSearch:flaskDataUserSearch})
    url2view.update({strDataMd5Search:None})
    
    url2view.update({strObjectDetails:flaskDataObjectDetail})
    url2view.update({strDisableObject:flaskDisableObject}) # db
    url2view.update({strEnableObject:flaskEnableObject}) # db
    
    url2view.update({strDeleteObject:flaskDeleteObject}) # restful
    url2view.update({strDownloadObject:flaskDownloadObject}) #restful
    url2view.update({strUploadObject:flaskUploadObject}) #restful
    url2view.update({strQuotaGet:flaskQuotaGet}) # restful
    url2view.update({strQuotaSet:flaskQuotaSet}) # restful
    
    url2view.update({strAccountList:flasklistAccount})   # db
    url2view.update({strContainerList:flasklistContainer})   #db
    url2view.update({strDirList:flasklistDir})   #db
    url2view.update({strGetAtRecords:flaskGetAccountRecords})   #db
    url2view.update({strGetOtRecords:flaskGetObjectRecords})    #db
    
    return url2view

