import time
import threading
import math
from Packet import *
from SelectiveRepeatWindow import *


class SenderWindow(Window):
   
    
    def __init__(self, message, sendPacket, getResponse):
        windowSize = math.ceil(len(message) / PAYLOAD_SIZE)
        super().__init__(windowSize, sendPacket, getResponse, 0)

        for i in range(0, self.windowSize):
            self.frameData[i] = message[i * PAYLOAD_SIZE:(i + 1) * PAYLOAD_SIZE]

    def process(self):
        timenow = time.time()

        # Check the window
        for i in range(self.windowStart, self.windowSize):
            if (not self.frameHandled[i]):
                if (timenow > (DEFAULT_WAIT_TIME + self.frameTimer[i])):
                    self.sendPacket(PACKET_TYPE_DATA, i, self.frameData[i])

        # Wait for feedback.
        while (True):
            response = self.getResponse()

            if (response is not None):
                print("Got response")
                self.handleResponse(response)
            else:
                print("No response")
                break

    def handleResponse(self, packet):
        
        # Figure out what kind of packet it is.
        packetType = packet.getPacketType();
        
        if (packetType == PACKET_TYPE_AK):
            print("fuck")
