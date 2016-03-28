
import subprocess

def sysCmd(argList):

    child = subprocess.Popen(argList,stdout=subprocess.PIPE)
    # communicate() returns a tuple (stdout, stderr)
    outStr,errStr = child.communicate()
    return outStr,errStr

if __name__ == '__main__':
    print sysCmd(['ls'])

    
    
