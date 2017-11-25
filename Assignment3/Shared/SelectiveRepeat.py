import time
import threading
import math
from Packet import *

DEFAULT_WAIT_TIME = 10 * 10000

class SelectiveRepeatSender:

    __windowSize = None 
    __windowStart = 0

    __frameAked = None
    __frameData = None
    __frameTimer = None

    __sendPacket = None
    __getResponse = None
    
    
    def __init__(self, message, sendPacket, getResponse):

        self.__sendPacket = sendPacket
        self.__getResponse = getResponse
        
        self.__windowSize = math.ceil(len(message) / PAYLOAD_SIZE)
        self.__frameAked = [False] * self.__windowSize
        self.__frameData = [None] * self.__windowSize
        self.__frameTimer = [0] * self.__windowSize

        for i in range(0, self.__windowSize):
            self.__frameData[i] = message[i * PAYLOAD_SIZE:(i + 1) * PAYLOAD_SIZE]

    def finishedSending(self):
        return False

    def process(self):
        timenow = time.time()

        # Check the window
        for i in range(self.__windowStart, self.__windowSize):
            if (not self.__frameAked[i]):
                if (timenow > (DEFAULT_WAIT_TIME + self.__frameTimer[i])):
                    self.__sendPacket(PACKET_TYPE_DATA, i, self.__frameData[i])

        # Wait for feedback.
        while (True):
            response = self.__getResponse()

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


    def __monitorWindow(self, timeoutcallback):
        while (True):
            for i in range(0, len(self.__windowData)):
                elapsedTime = time.time() - self.__timers[i]
                sequenceNumber = (self.__windowStart + i) %  1

                if (elapsedTime >= self.__timeout):
                    self.__timers[i] = time.time()
                    timeoutcallback()
