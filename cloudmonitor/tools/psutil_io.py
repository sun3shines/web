# -*- coding: utf-8 -*-

import sys
import time

def read(path):
    
    with file(path) as f:
        while True:
            chunk = f.read(4096)
            if chunk:
                yield chunk
            else:
                break
            
def write(path):
    
    with file(path,'w') as f:
        while True:
            chunk = (yield) 
            if chunk:
                f.write(chunk)
            else:
                import pdb;pdb.set_trace()
                break
            
        
def io_disk(path,bytes):

    total_bytes = 0 
    start_time = time.time()
    
    o = write(path+'.tmp') 
    next(o)
    
    while total_bytes < bytes:
        i = read(path)
        for chunk in i:
            total_bytes = total_bytes + len(chunk) 
            o.send(chunk)
            
            dural_time=float(time.time()) - float(start_time)
            if(dural_time>0):
                speed = float(total_bytes)/float(dural_time)/(1000*1000)
                while(speed >1):
                    time.sleep(0.1)
                    dural_time=float(time.time()) - float(start_time)
                    speed = float(total_bytes)/float(dural_time)/(1000*1000)
    o.send('') 

if __name__ == '__main__':
    argv = sys.argv            
    if len(argv) < 2:
        sys.exit(0)
    io_disk(argv[1],1024*1024*500)

