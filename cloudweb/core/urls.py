# -*- coding: utf-8 -*-

from cloudcommon.common.exceptions import LockTimeout, MessageTimeout
from cloudcommon.common.bufferedhttp import jresponse

from cloudweb.core.views.fs import *
from cloudweb.core.views.user import *
from cloudweb.core.views.search import *
from cloudweb.core.views.object import *
from cloudweb.core.views.quota import *
from cloudweb.core.views.host import *
from cloudweb.core.views.config import *
from cloudweb.core.views.record import *
from cloudweb.core.views.record import getObjectRecords, getAccountRecords


url2view = {}

strUserLogin = '/api/user/login'
url2view.update({strUserLogin:userLogin}) # restful

strUserList = '/api/user/list'
url2view.update({strUserList:userList})

strUserEnable = '/api/user/enable'
url2view.update({strUserEnable:userEnable})

strUserDisable = '/api/user/disable'
url2view.update({strUserDisable:userDisable})

strUserDelete = '/api/user/delete'
url2view.update({strUserDelete:userDelete})

strGetServiceStatus = '/api/host/getServiceStatus'
url2view.update({strGetServiceStatus:None})

strGetWorkloadStatus = '/api/host/getWorkloadStatus'
url2view.update({strGetWorkloadStatus:None})

strGetAbnormalEvents = '/api/host/getAbnormalEvents'
url2view.update({strGetAbnormalEvents:None})

strDataGlobalSearch = '/api/data/dataGlobalSearch'
url2view.update({strDataGlobalSearch:dataGlobalSearch})

strDataUserSearch = '/api/data/dataUserSearch'
url2view.update({strDataUserSearch:dataUserSearch})

strDataMd5Search = '/api/data/dataMd5Search'
url2view.update({strDataMd5Search:None})

strObjectDetails = '/api/data/objectDetails'
url2view.update({strObjectDetails:dataObjectDetail})

strDisableObject = '/api/data/disableObject'
url2view.update({strDisableObject:disableObject}) # db

strEnableObject = '/api/data/enableObject'
url2view.update({strEnableObject:enableObject}) # db

strDeleteObject = '/api/data/deleteObject'
url2view.update({strDeleteObject:deleteObject}) # restful

strDownloadObject = '/api/data/downloadObject'
url2view.update({strDownloadObject:downloadObject}) #restful

strUploadObject = '/api/data/uploadObject'
url2view.update({strUploadObject:uploadObject}) #restful

strQuotaGet = '/api/quota/quotaGet'
url2view.update({strQuotaGet:quotaGet}) # restful

strQuotaSet = '/api/quota/quotaSet'
url2view.update({strQuotaSet:quotaSet}) # restful

strAccountList='/api/fs/listAccount'    
url2view.update({strAccountList:listAccount})   # db

strContainerList = '/api/fs/listContainer'
url2view.update({strContainerList:listContainer})   #db

strDirList = '/api/fs/listDir'
url2view.update({strDirList:listDir})   #db

strGetAtRecords = '/api/record/account'
url2view.update({strGetAtRecords:getAccountRecords})   #db

strGetOtRecords = '/api/record/object'
url2view.update({strGetOtRecords:getObjectRecords})    #db

def handlerequest(req,sdata):
    url = req.path
    if url not in url2view:
        return jresponse('-1','url error',req,404)
    return url2view[url](req,sdata)


