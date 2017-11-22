import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind(("localhost", 80))

while (True):
        data, addr = soc.recvfrom(1024)
        print (data)
