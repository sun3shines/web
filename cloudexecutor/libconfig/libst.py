# -*- coding: utf-8 -*-

import ConfigParser

def _stget(path,sec,option):
    
    conf = ConfigParser.ConfigParser()
    conf.read(path)
    return conf.get(sec,option)
    
def _stset(path,sec,option,val):
    
    conf = ConfigParser.ConfigParser()
    conf.read(path)
    conf.set(sec,option,val)
    conf.write(open(path,'w'))
    
   
if __name__ == '__main__':
    p = '/etc/swift/proxy-server.conf'
    sec = 'DEFAULT'
    option = 'workers'
    print _stget(p,sec,option)
    
    _stset(p,sec,option,'1')
