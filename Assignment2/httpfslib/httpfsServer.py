import time
import threading
from httpfsLogger import *
from requestHandler import *
from ReceiverController import *
from SenderController import *

class httpfsServer:

    __logger = None
    __port = None
    __path = None
    
    def __init__(self, verbose, port, path):
        self.__logger = ConsoleLogger(verbose)
        self.__port = port
        self.__path = path

    def start(self):
        try:
            self.log("Httpfs server is listening at {0}".format(self.__port))

            while True:
                rc = ReceiverController(self.__port)
                self.log("Got connection")
                message = rc.getMessage()
                response = requestHandler(message, self.__path).getResponse().getFullHttpRequest()

                sc = SenderController(rc.address[0], rc.address[1])
                sc.sendMessage(response)
                self.log("Closing connection")
            
        finally:
            self.log("Something went wrong")
            
    def log(self, message):
        self.__logger.displayMessage(message)
