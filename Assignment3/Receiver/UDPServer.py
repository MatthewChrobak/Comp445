import socket
#import ReceiverController

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))
#receiverController = ReceiverController()

print("Server is ready")

while True:
	data, address = serverSocket.recvfrom(1024)
	#if(len(data) > 0):

	






	newMsg = "Server received " + message.decode('utf-8')
	serverSocket.sendto(newMsg.encode('utf-8'), address)



