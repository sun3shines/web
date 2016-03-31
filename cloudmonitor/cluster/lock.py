
from clusterConfig import lockCache
import threading

def getLock(lockName):

    if not lockCache.get(lockName):
        lockCache[lockName] = threading.Lock()
    
    return lockCache[lockName]

