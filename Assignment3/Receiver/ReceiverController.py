import socket
import Packet

class ReceiverController:
	
	__socketRC = NULL
	__ACK = NULL
	
	__window = NULL
	__timer = NULL
	__MaxWindowSize = NULL
	

	def __init__(self):
		self.__window = []
		self.__timer = []
		__socketRC = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


	def convertDataToPacket(self, data):
		
		packetType = int.from_bytes(data[0], 'big')
		packetSN = int.from_bytes(data[1:5], 'big')
		packetDestinationAddress = int.from_bytes(data[5:9], 'big')
		packetDestinationPort = int.from_bytes(data[9:11], 'big')
		packetPayload = data[11:].decode('utf-8')

		reassembledPacket = Packet(packetType, packetSN, packetDestinationAddress, packetDestinationPort, packetPayload)
		return reassembledPacket		


	def reliableDataTrans(self, packet):

		if(packet.getPacketType == 1):
			if(self.__ACK == True):
			{
				if(len(self.__window) < self.__MaxWindowSize):
					self.__window.append(packet)
			}

		

		if(packet.getPacketType == 2):
			packet.setPacketType(3)
			senderAddress = packet.getDestinationAddress()
			self.__socketRC.sendto(packet, senderAddress)

		
		if(packet.getPacketType == 4):
			self.__ACK = True

