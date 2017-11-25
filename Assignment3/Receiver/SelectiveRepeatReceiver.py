from SelectiveRepeatWindow import *

class ReceiverWindow(Window):

    def __init__(self, windowSize, sendPacket, getResponse):
        super().__init__(windowSize, sendPacket, getResponse)
        

    def finished(self):
        for i in range(0, self.windowSize):
            if not self.frameHandled[i]:
                return False

        return True

    def process(self):
        timenow = time.time()

        # Check the window
        for i in range(self.windowStart, self.windowSize):
            if (not self.frameHandled[i]):
                if (timenow > (DEFAULT_WAIT_TIME + self.frameTimer[i])):
                    self.sendPacket(PACKET_TYPE_AK, i - 1, "")

                break

        # Wait for incoming data
        while (True):
            response = self.getResponse(1)

            if (response is not None):
                self.handleResponse(response)
            else:
                print("No response")
                break

    def handleResponse(self, packet):
        if (packet.getPacketType() == PACKET_TYPE_DATA):
            seq = packet.getSequenceNumber()

            self.frameData[seq] = packet.getPayload()
            self.frameHandled[seq] = True
