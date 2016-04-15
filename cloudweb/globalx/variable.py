# -*- coding: utf-8 -*-

from cloudweb.db.table.lock.mysql import getdb
from cloudlib.advanced.cachedb import CacheDb

GLOBAL_USER_DB = CacheDb(getdb)
