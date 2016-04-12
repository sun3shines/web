# -*- coding: utf-8 -*-

from cloudlib.advanced.lockdict import lockDict

GlobalDb = lockDict()

GlobalThread = lockDict()

GlobalQueue = lockDict()

GlobalClass = ['host','statCpu','statMem','statNet','statDisk','statStorage',
               'statService']

MIRROR_LIMIT = 100
