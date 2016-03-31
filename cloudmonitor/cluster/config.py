
srvInterval = 3
srvFailed = 9
timeCfgPath = 'TimeStamp.cfg'
mountCmd = 'mount'
userCifsStoragePath = '/mnt/cifs'
userCifsStorageDevice = '//192.168.36.55/test'

userCephStoragePath = ''
userCephStorageDevice = ''

userBusinessPath = 'ff89f933b2ca8df40'
mountStatusInterval = 5

ifconfigExpr = ''
ethtoolExpr = ''

ipExprPtn = r'inet addr:([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})'
macExprPtn = r'HWaddr ([0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2})'
maskExprPtn = r'Mask:([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})'
devExprPtn = r'(\w+)\s+Link encap'
linkExprPtn = r'Link detected:\s(\w+)'

fileBlockSize = 1024

mongoHost = '127.0.0.1'
mongoPort = 27017
mongoDb = 'cacheData'

memCache = {}
lockCache = {}


