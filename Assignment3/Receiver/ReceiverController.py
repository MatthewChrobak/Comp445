from socket import *
from Packet import *
from PacketDecoder import *
from PacketBuilder import *

class ReceiverController:
    
    __socketRC = None
    __routerAddr = ('127.0.0.1', 3000)
    __packetBuilder = None

    def __init__(self, port):
        self.__socketRC = socket(AF_INET, SOCK_DGRAM)
        self.__socketRC.bind(('', port))
        print("Listening")

    def sendPacket(self, packetType, sequenceNumber, content, address):
        packet = self.__packetBuilder.build(packetType, sequenceNumber, content)
        self.__socketRC.sendto(packet.getBytes(), address)

    def getPacket(self):
        data, addr = self.__socketRC.recvfrom(PACKET_SIZE)
        pkt = PacketDecoder.decode(data)

        print(pkt.getDestinationAddress())

        if (self.__packetBuilder is None):
            self.__packetBuilder = PacketBuilder(pkt.getDestinationAddress(), pkt.getDestinationPort())
        
        print(data)
        return pkt

    def buildConnection(self):
        packet = self.getPacket()

        if (packet.getPacketType() == PACKET_TYPE_SYN):
            addr = (packet.getDestinationAddress(), packet.getDestinationPort())
            self.sendPacket(PACKET_TYPE_SYN_AK, 1, "", addr)

            packet = self.getPacket()

            if (packet.getPacketType() == PACKET_TYPE_AK):
                return True

        return False

    def getMessage(self):
        # Make sure we have some connection.
        if (self.buildConnection()):
            while (True):
                packet = self.getPacket()

                if (packet.getPacketType() == PACKET_TYPE_DATA):
                    print("I got something")


