import time
import threading
import math
from Packet import *

DEFAULT_WAIT_TIME = 10

class Window:

    __windowSize = None 
    __windowStart = 0

    __frameHandled = None
    __frameData = None
    __frameTimer = None

    __sendPacket = None
    __getResponse = None

    def __init__(self, windowSize, sendPacket, getResponse):
        self.__windowSize = windowSize
        self.__sendPacket = sendPacket
        self.__getResponse = getResponse

        self.__frameAked = [False] * self.__windowSize
        self.__frameData = [None] * self.__windowSize
        self.__frameTimer = [0] * self.__windowSize

        for i in range(0, self.__windowSize):
            self.__frameData[i] = message[i * PAYLOAD_SIZE:(i + 1) * PAYLOAD_SIZE]
        

    def finished(self):
        for i in range(0, self.__windowSize):
            if not self.__frameHandled[i]:
                return False

        return True

    def process(self):
        print("No process specified")

    def handleResponse(self, packet):
        print("No handleResponse specified")
