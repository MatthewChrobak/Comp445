from socket import *
from Packet import *
from PacketDecoder import *
from PacketBuilder import *

class ReceiverController:
    
    __socketRC = None
    __packetBuilder = None

    def __init__(self, port):
        self.__socketRC = socket(AF_INET, SOCK_DGRAM)
        self.__socketRC.bind(('', port))
        self.__packetBuilder = PacketBuilder('127.0.0.1', 80)
        print("Listening")

    def sendPacket(self, packetType, sequenceNumber, content, address):
        packet = self.__packetBuilder.build(packetType, sequenceNumber, content)
        self.__socketRC.sendto(packet.getBytes(), address)

    def getPacket(self):
        data, addr = self.__socketRC.recvfrom(PACKET_SIZE)
        return PacketDecoder.decode(data)

    def buildConnection(self):
        packet = self.getPacket()

        if (packet.getPacketType() == PACKET_TYPE_SYN):
            print("Got syn")
            self.sendPacket(PACKET_TYPE_SYN_ACK, 1, "", (packet.getDestinationAddress(), packet.getDestinationPort()))

            packet = self.getPacket()

            if (packet.getPacketType() == PACKET_TYPE_AK):
                print("Got ak")
                return True

        return False

    def getMessage(self):
        # Make sure we have some connection.
        if (self.buildConnection()):
            while (True):
                packet = self.getPacket()

                if (packet.getPacketType() == PACKET_TYPE_DATA):
                    print("I got something")


