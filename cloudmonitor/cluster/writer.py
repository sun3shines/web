
import time
from clusterConfig import timeCfgPath,srvInterval

def write_srv_time():
    while True:
        fd = open(timeCfgPath,'w')
        fd.write(str(time.time()))
        fd.close()
        time.sleep(srvInterval)

if __name__ == '__main__':

    write_srv_time()
