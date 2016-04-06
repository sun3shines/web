# file write / read block

from cloudmonitor.cluster.config import fileBlockSize

def readBlock(fn):

    f = open(fn,'r')
    while True:
        data = f.read(fileBlockSize)
        if not data:
            break;
        print len(data)
        # do_something(data)

class STFile:

    def __init__(self,path):
        self.path = path
        self.handle = file(self.path)
        self.readsize = 1024

    def __iter__(self):

        try:
            while True:
                chunk = self.handle.read(self.readsize)        
                if chunk:
                    yield chunk
                else:
                    break
        finally:
            self.handle.close()

def make_file_iter(path,readsize=1024):
    
    handle = None 
    try:
        handle = file(path)
        while True:
            chunk = handle.read(readsize)
            if chunk:
                yield chunk
            else:
                break
    finally:
        if handle:
            handle.close()
 
if __name__ == '__main__':

#    readBlock('/var/log/messages')
#    stObj = STFile('/root/install.log')
#    for data in stObj:
#        print len(data) 
#        print data

    stObj = make_file_iter('/root/install.log11')
    for data in stObj:
        print len(data)
        print data


