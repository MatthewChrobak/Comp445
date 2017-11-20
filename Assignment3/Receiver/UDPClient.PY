import socket

serverName = 'localhost'
serverPort = 12000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = 'data test on client side'
clientSocket.sendto(data.encode('utf-8'), (serverName, serverPort))

dataReceive, serverAddress = clientSocket.recvfrom(1024)
print(dataReceive.decode('utf-8'))
clientSocket.close()
