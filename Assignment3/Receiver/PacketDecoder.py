from Packet import *

class PacketDecoder:
	
	def decode(self, b_packet):
		packetType = int.from_bytes([b_packet[0]], 'big')
		packetSN = int.from_bytes(b_packet[1:5], 'big')
		addressP1 = int.from_bytes([b_packet[5]], 'big')
		addressP2 = int.from_bytes([b_packet[6]], 'big')
		addressP3 = int.from_bytes([b_packet[7]], 'big')
		addressP4 = int.from_bytes([b_packet[8]], 'big')
		packetDestinationAddress = str(addressP1) + '.' + str(addressP2) + '.' + str(addressP3) + '.' + str(addressP4)
		packetDestinationPort = int.from_bytes(b_packet[9:11], 'big')
		packetPayload = b_packet[11:].decode('utf-8')
		decodedPacket = Packet(packetType, packetSN, packetDestinationAddress, packetDestinationPort, packetPayload)
		return decodedPacket