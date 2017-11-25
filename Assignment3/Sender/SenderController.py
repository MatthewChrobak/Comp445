from socket import *
from Packet import *
from PacketBuilder import *
from PacketDecoder import *
from SelectiveRepeatSender import *

class SenderController:
    __window = None
    __socket = None
    __addr = None
    __routerAddr = ('127.0.0.1', 3000)
    __packetBuilder = None
    __port = None


    def __init__(self, ip, port):
        if (str(ip).lower() == "localhost"):
            ip = "127.0.0.1"

        self.__packetBuilder = PacketBuilder(ip, port)
        self.__addr = (ip, port)

    def sendMessage(self, message):
        self.__socket = socket(AF_INET, SOCK_DGRAM)
        self.__socket.settimeout(1)
        self.__window = SenderWindow(message, self.sendPacket, self.getResponse)

        if self.connect(self.__window.windowSize):
            print("Connected")

            while not self.__window.finished():
                self.__window.process()
        else:
            print("Could not establish a connection")

        self.__port = self.__socket.getsockname()[1]
        self.__socket.close()


    def sendPacket(self, packetType, sequenceNumber, content):
        print("Sending packet type: " + str(packetType) + " with #" + str(sequenceNumber))
        packet = self.__packetBuilder.build(packetType, sequenceNumber, content)
        self.__socket.sendto(packet.getBytes(), self.__routerAddr)

    def getResponse(self):
        try:
            data, addr = self.__socket.recvfrom(PACKET_SIZE)
            packet = PacketDecoder.decode(data)
            print("Got packet type: " + str(packet.getPacketType()) + " with #" + str(packet.getSequenceNumber()))
            return packet
        except Exception as e:
            print(e)
            return None
        
    def connect(self, windowSize):
        for i in range(0, 5):
            print("Trying to connect: " + str(i))
            self.sendPacket(PACKET_TYPE_SYN, 0, "")
            response = self.getResponse()

            if (response is not None and response.getPacketType() == PACKET_TYPE_SYN_AK):
                self.sendPacket(PACKET_TYPE_AK, 0, str(windowSize))
                return True

        return False

    def getSocketPort(self):
        return self.__port
