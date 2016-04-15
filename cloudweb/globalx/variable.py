# -*- coding: utf-8 -*-

from cloudweb.db.table.mysql import getDb
from cloudlib.advanced.cachedb import CacheDb

GLOBAL_USER_DB = CacheDb(getDb)
