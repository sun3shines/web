# -*- coding: utf-8 -*-

from cloudlib.common.exceptions import LockTimeout, MessageTimeout
from cloudlib.common.bufferedhttp import jresponse
from cloudlib.urls.flask import *

from cloudweb.platform.http_flask_fs import *
from cloudweb.platform.http_flask_user import *
from cloudweb.platform.http_flask_search import *
from cloudweb.platform.http_flask_object import *
from cloudweb.platform.http_flask_quota import *
from cloudweb.platform.http_flask_host import *
from cloudweb.platform.http_flask_config import *
from cloudweb.platform.http_flask_record import *
from cloudweb.platform.http_flask_record import url_getObjectRecords, url_getAccountRecords


url2view = {}

url2view.update({strUserLogin:url_userLogin}) # restful

url2view.update({strUserList:url_userList})

url2view.update({strUserEnable:url_userEnable})

url2view.update({strUserDisable:url_userDisable})

url2view.update({strUserDelete:url_userDelete})

url2view.update({strGetServiceStatus:None})

url2view.update({strGetWorkloadStatus:None})

url2view.update({strGetAbnormalEvents:None})

url2view.update({strDataGlobalSearch:url_dataGlobalSearch})

url2view.update({strDataUserSearch:url_dataUserSearch})

url2view.update({strDataMd5Search:None})

url2view.update({strObjectDetails:url_dataObjectDetail})

url2view.update({strDisableObject:url_disableObject}) # db

url2view.update({strEnableObject:url_enableObject}) # db

url2view.update({strDeleteObject:url_deleteObject}) # restful

url2view.update({strDownloadObject:url_downloadObject}) #restful

url2view.update({strUploadObject:url_uploadObject}) #restful

url2view.update({strQuotaGet:url_quotaGet}) # restful

url2view.update({strQuotaSet:url_quotaSet}) # restful

url2view.update({strAccountList:url_listAccount})   # db

url2view.update({strContainerList:url_listContainer})   #db

url2view.update({strDirList:url_listDir})   #db

url2view.update({strGetAtRecords:url_getAccountRecords})   #db

url2view.update({strGetOtRecords:url_getObjectRecords})    #db

def handlerequest(req,sdata):
    url = req.path
    if url not in url2view:
        return jresponse('-1','url error',req,404)
    return url2view[url](req,sdata)


