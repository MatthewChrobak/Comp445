from socket import *
from Packet import *
from PacketBuilder import *

class SenderController:
    __window = None
    __socket = None
    __addr = None
    __packetBuilder = None


    def __init__(self, ip, port):
        self.__socket = socket(AF_INET, SOCK_DGRAM)

        if (str(ip).lower() == "localhost"):
            ip = "127.0.0.1"

        self.__packetBuilder = PacketBuilder(ip, port)
        self.__addr = (ip, port)

    def sendMessage(self, message):
        self.__connect()

        # Todo: Send the window. Check if connected.

    def sendPacket(self, packetType, sequenceNumber, content):
        packet = self.__packetBuilder.build(packetType, sequenceNumber, content)
        self.__socket.sendto(packet.getBytes(), self.__addr)


    def __connect(self):
        self.sendPacket(PACKET_TYPE_SYN, 1, "")

        # Denotes that we connected. Assume true for now.
        return True
