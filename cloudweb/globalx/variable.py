# -*- coding: utf-8 -*-

from cloudweb.db.table.mysql import getDb
from cloudlib.advanced.cachedb import CacheDb
from cloudlib.advanced.cacheuser import CacheUser
from cloudlib.advanced.cacheconsistency import CacheConsistency

GLOBAL_USER_DB = CacheDb(getDb)

GLOBAL_USER_TOKEN = CacheUser()
GLOBAL_USER_CONSISTENCY = CacheConsistency()
