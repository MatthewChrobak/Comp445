import socket
from Packet import *
from PacketDecoder import *

PACKET_TYPE_DATA = 1
PACKET_TYPE_SYN = 2
PACKET_TYPE_SYN_AK = 3
PACKET_TYPE_AK = 4

SYN = False
SYN_ACK = False
ACK = False

serverName = '172.31.52.111'
serverPort = 80
clientPacketDecoder = PacketDecoder()

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.bind(('', 1000)) #specify a fixed port number for sender

#----generate simple packet to interact with server
pkt1 = Packet(PACKET_TYPE_SYN, 0, serverName, serverPort, "Sender First Packet: SYN")
pkt2 = Packet(PACKET_TYPE_AK, 0, serverName, serverPort, "Sender Second Packet: ACK")
pkt3 = Packet(PACKET_TYPE_DATA, 0, serverName, serverPort, "Sender Third Packet: DATA")

bytePkt1 = pkt1.getBytes()
bytePkt2 = pkt2.getBytes()
bytePkt3 = pkt3.getBytes()

while True:

	if(SYN == False):
		clientSocket.sendto(bytePkt1, (serverName, serverPort))
		SYN = True
	
	dataReceived, serverAddress = clientSocket.recvfrom(1024)
	serverPacket = clientPacketDecoder.decode(dataReceived)
	message = serverPacket.getPayload()
	print(message)
	
	if(serverPacket.getPacketType == PACKET_TYPE_SYN_AK):
		SYN_ACK = True
		clientSocket.sendto(bytePkt2, (serverName, serverPort))
		clientSocket.sendto(bytePkt3, (serverName, serverPort))
	
	
#dataReceive, serverAddress = clientSocket.recvfrom(1024)
#print(dataReceive.decode('utf-8'))
#clientSocket.close()




