
import socket

def getHostName():

    return socket.gethostname()
    
if __name__ == '__main__':

    print getHostName()
