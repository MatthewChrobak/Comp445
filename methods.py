import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(("172.217.10.3", 80))

soc.send("GET / HTTP/1.1\r\nHost: www.google.ca\r\n\r\n".encode("utf-8"))
response = soc.recv(1000000)
print(response)
