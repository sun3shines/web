# -*- coding: utf-8 -*-

from cloudcommon.common.exceptions import LockTimeout, MessageTimeout
from cloudcommon.common.bufferedhttp import jresponse
from cloudcommon.urls.web import *

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

url2view.update({strUserLogin:userLogin}) # restful

url2view.update({strUserList:userList})

url2view.update({strUserEnable:userEnable})

url2view.update({strUserDisable:userDisable})

url2view.update({strUserDelete:userDelete})

url2view.update({strGetServiceStatus:None})

url2view.update({strGetWorkloadStatus:None})

url2view.update({strGetAbnormalEvents:None})

url2view.update({strDataGlobalSearch:dataGlobalSearch})

url2view.update({strDataUserSearch:dataUserSearch})

url2view.update({strDataMd5Search:None})

url2view.update({strObjectDetails:dataObjectDetail})

url2view.update({strDisableObject:disableObject}) # db

url2view.update({strEnableObject:enableObject}) # db

url2view.update({strDeleteObject:deleteObject}) # restful

url2view.update({strDownloadObject:downloadObject}) #restful

url2view.update({strUploadObject:uploadObject}) #restful

url2view.update({strQuotaGet:quotaGet}) # restful

url2view.update({strQuotaSet:quotaSet}) # restful

url2view.update({strAccountList:listAccount})   # db

url2view.update({strContainerList:listContainer})   #db

url2view.update({strDirList:listDir})   #db

url2view.update({strGetAtRecords:getAccountRecords})   #db

url2view.update({strGetOtRecords:getObjectRecords})    #db

def handlerequest(req,sdata):
    url = req.path
    if url not in url2view:
        return jresponse('-1','url error',req,404)
    return url2view[url](req,sdata)


