from Packet import *

class PacketBuilder:
        __destinationAddress = None
        __destinationPort = None

        def __init__(self, destinationAddress, destinationPort):
                self.__destinationAddress = destinationAddress
                self.__destinationPort = destinationPort

        def build(self, packetType, sequenceNumber, payload):
                return Packet(packetType, sequenceNumber, self.__destinationAddress, self.__destinationPort, payload)
