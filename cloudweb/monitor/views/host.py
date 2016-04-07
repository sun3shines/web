# -*- coding: utf-8 -*-

import json
import Queue

from cloudcommon.common.bufferedhttp import jresponse
from cloudweb.db.table.static.host import puth,uuid2hostid
from cloudweb.db.table.static.host_cpu import putc
from cloudweb.db.table.static.host_mem import putms
from cloudweb.db.table.static.host_net import putns
from cloudweb.db.table.static.host_disk import putds

from cloudweb.monitor.globalx import GlobalDb,GlobalQueue,GlobalThread,GlobalClass
from cloudweb.db.table.lock.mysql import getdb,getlock
from cloudweb.monitor.threads.cpu import StatCpu
from cloudweb.monitor.threads.mem import StatMem
from cloudweb.monitor.threads.net import StatNet
from cloudweb.monitor.threads.disk import StatDisk
from cloudweb.monitor.threads.storage import StatStorage

def processStartUp(request,sdata):

    param = json.loads(request.body)
    
    hostUuid = param.get('hostUuid')
    if not GlobalDb.get(hostUuid):
        GlobalDb.put(hostUuid, getdb())
        
    db = GlobalDb.get(hostUuid)
    
    with getlock(db) as mylock:
        puth(db,hostUuid,param.get('hostClass'))
        hostid = uuid2hostid(db, hostUuid)
        putc(db, hostid, param.get('cpuClass'))
        putms(db, hostid, param.get('memClass'))
        putns(db, hostid, param.get('netClass'))
        putds(db, hostid, param.get('diskClass'))
    
    if not GlobalQueue.get(hostUuid):
        loadQueue(hostUuid, GlobalQueue)
        
    if not GlobalThread.get(hostUuid):
        loadThread(db,hostUuid, GlobalThread)
    
    return jresponse('0','ready',request,200)

def loadQueue(hostUuid,queueDict):
    
    queueDict.put(hostUuid,{})
    for cls in GlobalClass:
        queueDict.get(hostUuid).update({cls:Queue.Queue()})
        
def loadThread(db,hostUuid,threadDict):
    
    StatCpu(db,hostUuid).start()
    StatMem(db,hostUuid).start()
    StatDisk(db,hostUuid).start()
    StatNet(db,hostUuid).start()
    StatStorage(db,hostUuid).start()
    
    
