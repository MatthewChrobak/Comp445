from socket import *
from Packet import *
from PacketDecoder import *
from PacketBuilder import *
from SelectiveRepeatReceiver import *

class ReceiverController:
    
    __socketRC = None
    __routerAddr = ('127.0.0.1', 3000)
    __packetBuilder = None
    __window = None

    def __init__(self, port):
        self.__socketRC = socket(AF_INET, SOCK_DGRAM)
        self.__socketRC.bind(('', port))
        print("Listening")

    def sendPacket(self, packetType, sequenceNumber, content):
        print("Sending packet type: " + str(packetType) + " with #" + str(sequenceNumber))
        packet = self.__packetBuilder.build(packetType, sequenceNumber, content)
        self.__socketRC.sendto(packet.getBytes(), self.__routerAddr)

    def getPacket(self, timeout = None):
        self.__socketRC.settimeout(timeout)
        try:
            data, addr = self.__socketRC.recvfrom(PACKET_SIZE)
        except Exception as e:
            print(e)
            return None
        pkt = PacketDecoder.decode(data)
        print("Got packet type: " + str(pkt.getPacketType()) + " with #" + str(pkt.getSequenceNumber()))

        if (self.__packetBuilder is None):
            self.__packetBuilder = PacketBuilder(pkt.getDestinationAddress(), pkt.getDestinationPort())
        
        return pkt

    def buildConnection(self):
        packet = self.getPacket()

        if (packet.getPacketType() == PACKET_TYPE_SYN):
            addr = (packet.getDestinationAddress(), packet.getDestinationPort())
            self.sendPacket(PACKET_TYPE_SYN_AK, 1, "")

            packet = self.getPacket()

            if (packet.getPacketType() == PACKET_TYPE_AK):
                return True

        return False

    def getMessage(self):
        # Make sure we have some connection.
        if (self.buildConnection()):
            self.__window = ReceiverWindow(3, self.sendPacket, self.getPacket)
            
            while not self.__window.finished():
                self.__window.process()


