PACKET_TYPE_NONE = 0
PACKET_TYPE_DATA = 1
PACKET_TYPE_SYN = 2
PACKET_TYPE_SYN_AK = 3
PACKET_TYPE_AK = 4

PACKET_TYPE_SIZE = 1
SEQUENCE_SIZE = 4
DESTINATION_ADDRESS_SIZE = 4
DESTINATION_PORT_SIZE = 2
PAYLOAD_SIZE = 1013
PACKET_SIZE = PACKET_TYPE_SIZE + SEQUENCE_SIZE + DESTINATION_ADDRESS_SIZE + DESTINATION_PORT_SIZE + PAYLOAD_SIZE


class Packet:

	__packetType = PACKET_TYPE_NONE
	__sequenceNumber = -1
	__destinationAddress = None
	__destinationPort = None
	__payload = None


	def __init__(self, packetType, sequenceNumber, destinationAddress, destinationPort, payload):
		self.setPacketType(packetType)
		self.setSequenceNumber(sequenceNumber)
		self.setDestinationAddress(destinationAddress)
		self.setDestinationPort(destinationPort)
		self.setPayload(payload)

	def getPacketType(self):
		return self.__packetType

	def setPacketType(self, packetType):
		self.__packetType = packetType

	def getSequenceNumber(self):
		return self.__sequenceNumber

	def setSequenceNumber(self, sequenceNumber):
		self.__sequenceNumber = int(sequenceNumber)

	def getDestinationAddress(self):
		return self.__destinationAddress

	def setDestinationAddress(self, destinationAddress):
		if (str(destinationAddress).lower() is 'localhost'):
			destinationAddress = "127.0.0.1"

		self.__destinationAddress = str(destinationAddress)

	def getDestinationPort(self):
		return int(self.__destinationPort)

	def setDestinationPort(self, destinationPort):
		self.__destinationPort = int(destinationPort)

	def getPayload(self):
		return self.__payload

	def setPayload(self, payload):
		if (len(payload) > PAYLOAD_SIZE):
			raise Exception("Invalid payload size {0}".format(str(len(payload))))
		
		# Set the payload, and pad it with whitespace until all 1013 bytes are used.
		self.__payload = "{0}{1}".format(payload, ' ' * (PAYLOAD_SIZE - len(payload)))

	def getBytes(self):
		lstData = list()

		lstData.append(self.getPacketType().to_bytes(PACKET_TYPE_SIZE, 'big'))
		lstData.append(self.getSequenceNumber().to_bytes(SEQUENCE_SIZE, 'big', signed = True))

		# We assume the destination address is a string. We need to convert it into bytes. Get each number.
		ipaddr = self.getDestinationAddress().split('.')

		for i in range(0, 4):
			lstData.append(int(ipaddr[i]).to_bytes(1, 'big'))

		lstData.append(self.getDestinationPort().to_bytes(2, 'big'))
		lstData.append(self.__payload.encode("utf-8"))

		byteData = bytearray()

		for entry in lstData:
			for byte in entry:
				byteData.append(byte)

		return byteData
