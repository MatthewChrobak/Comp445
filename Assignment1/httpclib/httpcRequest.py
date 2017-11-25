from ReceiverController import *
from SenderController import *
import time
import re

class HttpcRequest:

    __httpMessage = None
    __connection = None
    __verbose = False
    __outputfilepath = None

    __sc = None

    def __init__(self, host, port, message, verbose = False, outputfilepath = None):
        self.__sc = SenderController(host, port)
        self.__httpMessage = message
        self.__verbose = verbose
        self.__outputfilepath = outputfilepath

    def execute(self):
        self.__sc.sendMessage(self.__httpMessage)

    def getResponse(self):
        rc = ReceiverController(self.__sc.getSocketPort())
        message = rc.getMessage()
        
        splitMessage = message.split("\r\n\r\n")


        header = splitMessage[0]
        body = "\r\n".join(splitMessage[1:])

        regex = r"HTTP\/1.1\s30[012]"
        match = re.search(regex, header)

        if match:
            regex = r"Location: (.+)"
            match = re.search(regex, header)

            newArgs = match.group(1)
            return newArgs


        if self.__verbose:
            print(header)
            print("\r\n")
            print(body)

        if self.__outputfilepath is not None:
            fs = open(self.__outputfilepath, "w")
            fs.write(header)
            fs.write('\r\n')
            fs.write(body)
            fs.close()
        return None
