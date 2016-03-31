
from clusterConfig import userCifsStoragePath,mountCmd,userCifsStorageDevice, \
userBusinessPath,mountStatusInterval

from clusterMsg import storageExistsMsg,storageNotExistsMsg,businessExistsMsg,businessNotExistsMsg, \
mountStatusSucMsg,mountStatusFailedMsg


from cmdExe import sysCmd
import os.path

def getMountStatus(userStoragePath,userStorageDevice):

    argList = [mountCmd]
    outStr,errStr = sysCmd(argList)
    if errStr:
        return False,errStr
    
    for line in outStr.split('\n'):
        infoList = line.split()    
        if len(infoList) != 6:
            continue
        sysStorageDevice = infoList[0]
        sysStoragePath = infoList[2] 
        sysFsType = infoList[4]
        sysFsFlag = infoList[5]
        
        if sysStorageDevice == userStorageDevice and sysStoragePath == userStoragePath:
            return True,storageExistsMsg

    return False,storageNotExistsMsg

def getBusinessStatus(userStoragePath,userBusinessPath):

    filePath = '%s/%s' % (userStoragePath,userBusinessPath)
    if os.path.exists(filePath):
        return True,businessExistsMsg
    else:
        return False,businessNotExistsMsg

def mountStatus():

    while True:
        flag,reasonMsg = getMountStatus(userCifsStoragePath,userCifsStorageDevice)
        if not flag:
            print reasonMsg
            print mountStatusFaildMsg
            time.sleep(mountStatusInterval)
            continue 
        flag,reasonMsg = getBusinessStatus(userCifsStoragePath,userBusinessPath)
        if not flag:
            print raasonMsg
            print mountStatusFailedMsg
            time.sleep(mountStatusInterval)
            continue
        print mountStatusSucMsg            
            
if __name__ == '__main__':

    mountStatus() 
