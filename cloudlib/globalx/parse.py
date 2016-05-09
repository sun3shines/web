
import sys
import ConfigParser

CONF_GLOBAL_PATH = '/etc/cloud/globalx.conf'

def _stget(path,sec,option):
    
    conf = ConfigParser.ConfigParser()
    conf.read(path)
    return conf.get(sec,option)
    
    
def get_controller_host():
    
    option = _stget(CONF_GLOBAL_PATH, 'DEFAULT', 'controller_host')
    
    if not option:
        print 'global config error,service exit'
        sys.exit(0)
    return option

def get_proxy_host():
    option = _stget(CONF_GLOBAL_PATH, 'DEFAULT', 'proxy_host')
    
    if not option:
        print 'global config error,service exit'
        sys.exit(0)
    return option


def get_proxy_port():
    option = _stget(CONF_GLOBAL_PATH, 'DEFAULT', 'proxy_port')
    
    if not option:
        print 'global config error,service exit'
        sys.exit(0)
    return int(option)

if __name__ == '__main__':

    print get_controller_host()
    print get_proxy_host()
    print get_proxy_port()
