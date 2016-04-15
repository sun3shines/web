# -*- coding: utf-8 -*-

from cloudlib.urls.cloudfs import *
from cloudweb.platform.http_cloudfs_account import cloudfsAccountDelete,cloudfsAccountGet,\
    cloudfsAccountHead,cloudfsAccountMeta,cloudfsAccountPost,cloudfsAccountPut
from cloudweb.platform.http_cloudfs_container import cloudfsContainerDelete,cloudfsContainerGet,cloudfsContainerHead,\
    cloudfsContainerMeta,cloudfsContainerPost,cloudfsContainerPut
from cloudweb.platform.http_cloudfs_dir import cloudfsDirCopy,cloudfsDirDelete,cloudfsDirDeleteRecycle,cloudfsDirGet,\
    cloudfsDirMetaGet,cloudfsDirMove,cloudfsDirMoveRecycle,cloudfsDirPut,cloudfsDirReset
from cloudweb.platform.http_cloudfs_firewall import cloudfsAccountValid,cloudfsObjectValid
from cloudweb.platform.http_cloudfs_link import cloudfsLinkPut
from cloudweb.platform.http_cloudfs_object import cloudfsObjectCopy,cloudfsObjectDelete,cloudfsObjectDeleteRecycle,\
    cloudfsObjectGet,cloudfsObjectHead,cloudfsObjectMeta,cloudfsObjectMove,cloudfsObjectMoveRecycle,\
    cloudfsObjectPost,cloudfsObjectPut
    
def cloudfsUrl2View():
    
    url2view = {}
    url2view.update({strCloudfsAccountDelete:cloudfsAccountDelete})
#    url2view.update({strCloudfsAccountExists:cloudfsAccountExists})
    url2view.update({strCloudfsAccountGet:cloudfsAccountGet})
    url2view.update({strCloudfsAccountHead:cloudfsAccountHead})
    url2view.update({strCloudfsAccountMeta:cloudfsAccountMeta})
    url2view.update({strCloudfsAccountPost:cloudfsAccountPost})
    url2view.update({strCloudfsAccountPut:cloudfsAccountPut})
    
    url2view.update({strCloudfsAccountValid:cloudfsAccountValid})
    url2view.update({strCloudfsObjectValid:cloudfsObjectValid})
    
    url2view.update({strCloudfsContainerDelete:cloudfsContainerDelete})
    url2view.update({strCloudfsContainerPut:cloudfsContainerPut})
    url2view.update({strCloudfsContainerHead:cloudfsContainerHead})
    url2view.update({strCloudfsContainerPost:cloudfsContainerPost})
    url2view.update({strCloudfsContainerMeta:cloudfsContainerMeta})
    url2view.update({strCloudfsContainerGet:cloudfsContainerGet})

    url2view.update({strCloudfsDirCopy:cloudfsDirCopy})
    url2view.update({strCloudfsDirDelete:cloudfsDirDelete})
    url2view.update({strCloudfsDirReset:cloudfsDirReset})
    url2view.update({strCloudfsDirDeleteRecycle:cloudfsDirDeleteRecycle})
    url2view.update({strCloudfsDirMove:cloudfsDirMove})
    url2view.update({strCloudfsDirMoveRecycle:cloudfsDirMoveRecycle})
    url2view.update({strCloudfsDirPut:cloudfsDirPut})
    url2view.update({strCloudfsDirGet:cloudfsDirGet})
    url2view.update({strCloudfsDirMetaGet:cloudfsDirMetaGet})
    
    
    url2view.update({strCloudfsLinkPut:cloudfsLinkPut})
    
    url2view.update({strCloudfsObjectPut:cloudfsObjectPut})
    url2view.update({strCloudfsObjectDelete:cloudfsObjectDelete})
    url2view.update({strCloudfsObjectDeleteRecycle:cloudfsObjectDeleteRecycle})
    url2view.update({strCloudfsObjectCopy:cloudfsObjectCopy})
    url2view.update({strCloudfsObjectMove:cloudfsObjectMove})
    url2view.update({strCloudfsObjectMoveRecycle:cloudfsObjectMoveRecycle})
    url2view.update({strCloudfsObjectGet:cloudfsObjectGet})
    url2view.update({strCloudfsObjectHead:cloudfsObjectHead})
    url2view.update({strCloudfsObjectMeta:cloudfsObjectMeta})
    url2view.update({strCloudfsObjectPost:cloudfsObjectPost})
    return url2view
    
