
import time
import os.path

from clusterConfig import timeCfgPath,srvFailed,srvInterval 
from clusterMsg import srvFailedMsg,srvStartedMsg
def read_srv_time():
    if not os.path.exists(timeCfgPath):
        fd = open(timeCfgPath,'w')
        fd.write(str(time.time()))
        fd.close()

    while True: 
        fd = open(timeCfgPath,'r')
        timeStr = fd.read()
        fd.close()
        if int(float(time.time())) - int(float(timeStr)) > srvFailed:
            print srvFailedMsg
        else:
            print srvStartedMsg

        time.sleep(srvInterval)

if __name__ == '__main__':
    
    read_srv_time()


    
