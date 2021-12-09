import sys 
for x in range(0,256):
	sys.stdout.write ("\\x" + '{:02x}'.format(x))
