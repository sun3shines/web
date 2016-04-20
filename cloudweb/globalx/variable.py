# -*- coding: utf-8 -*-

# from cloudweb.db.table.mysql import getDb
from cloudweb.db.table.lock.mysql import getdb
from cloudlib.advanced.cachedb import CacheDb
from cloudlib.advanced.cacheuser import CacheUser
from cloudlib.advanced.cacheconsistency import CacheConsistency
from cloudlib.advanced.cachequeue import CacheQueue

GLOBAL_USER_DB = CacheDb(getdb)

GLOBAL_USER_TOKEN = CacheUser()
GLOBAL_USER_CONSISTENCY = CacheConsistency()

USER_CONSISTENCY_DIR = CacheQueue()

strTimeStamp = 'timestamp'
