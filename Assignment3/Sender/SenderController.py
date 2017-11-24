from socket import *
from Packet import *
from PacketBuilder import *
from PacketDecoder import *

class SenderController:
    __window = None
    __socket = None
    __addr = None
    __routerAddr = ('127.0.0.1', 3000)
    __packetBuilder = None


    def __init__(self, ip, port):
        self.__socket = socket(AF_INET, SOCK_DGRAM)

        if (str(ip).lower() == "localhost"):
            ip = "127.0.0.1"

        self.__packetBuilder = PacketBuilder(ip, port)
        self.__addr = (ip, port)

    def sendMessage(self, message):
        self.connect()
            

        # Todo: Send the window. Check if connected.

    def sendPacket(self, packetType, sequenceNumber, content):
        packet = self.__packetBuilder.build(packetType, sequenceNumber, content)
        self.__socket.sendto(packet.getBytes(), self.__routerAddr)

    def getResponse(self):
        data, addr = self.__socket.recvfrom(PACKET_SIZE)
        return PacketDecoder.decode(data)
        
    def connect(self):
        self.sendPacket(PACKET_TYPE_SYN, 0, "")
        response = self.getResponse()

        if (response.getPacketType() == PACKET_TYPE_SYN_AK):
            self.sendPacket(PACKET_TYPE_AK, 0, "")
            return True

        return False
