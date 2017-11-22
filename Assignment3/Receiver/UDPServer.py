import socket
from ReceiverController import *

serverPort = 80
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
receiverController = ReceiverController()

print("Server is listen at port: " + str(serverPort))

while True:
	data, address = serverSocket.recvfrom(1024)
	
	if(len(data) > 0):
		receiverController.receivePacket(data)




