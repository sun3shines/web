# -*- coding: utf-8 -*-

from cloudweb.advanced.lockdict import lockDict

GlobalDb = lockDict()

GlobalThread = lockDict()

GlobalQueue = lockDict()

GlobalClass = ['host','statCpu','statMem','statNet','statDisk','statStorage']