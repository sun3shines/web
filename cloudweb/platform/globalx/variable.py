# -*- coding: utf-8 -*-

from cloudweb.db.table.lock.mysql import getdb,getlock
from cloudlib.advanced.cachedb import CacheDb
from cloudlib.advanced.cacheuser import CacheUser
from cloudlib.advanced.cacheconsistency import CacheConsistency
from cloudlib.advanced.cachequeue import CacheQueue
from cloudlib.advanced.locklist import lockList

GLOBAL_USER_DB = CacheDb(getdb,getlock)

GLOBAL_USER_TOKEN = CacheUser()
GLOBAL_USER_CONSISTENCY = CacheConsistency()

USER_CONSISTENCY_DIR = CacheQueue()

strTimeStamp = 'timestamp'

GLOBAL_ADMIN_TOKENS = lockList()
