
import re

def exprSearch(exprPattern,objectStr):

    match = re.search(exprPattern,objectStr)
    return match

def exprFindAll(exprPattern,objectStr):

    match = re.search(exprPattern,objectStr)
    return match


if __name__ == '__main__':
#    contactInfo = 'Doe, John: 555-1212'
#    match = exprSearch(r'(\w+), \w+: (\S+)', contactInfo)

#    print exprFindAll(r'(\w+), (\w+): (\S+)', contactInfo)

    objStr = '''eth0      Link encap:Ethernet  HWaddr 00:0C:29:78:E0:8F  
          inet addr:192.168.36.3  Bcast:192.168.255.255  Mask:255.255.0.0
          inet6 addr: fe80::20c:29ff:fe78:e08f/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:136219 errors:0 dropped:0 overruns:0 frame:0
          TX packets:52122 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:95769821 (91.3 MiB)  TX bytes:5985776 (5.7 MiB)
'''
# [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}MAC:[0-9A-F]{2}-[0-9A-F]{2}-[0-9A-F]{2}-[0-9A-F]{2}-[0-9A-F]{2}-[0-9A-F]{2}
#    exprPtn = r'(\w+)\s+Link encap:(\w+)\s+HWaddr (\w+).*inet addr:(\w+).*Mask:(\w+)'
    # exprPtn = r'(\w+)\s+Link encap:(\w+)\s+HWaddr ([0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2})/s+inet addr:([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})'
    exprPtn = r'inet addr:([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})'
      
    match = exprSearch(exprPtn,objStr)

