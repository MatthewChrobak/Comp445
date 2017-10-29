import socket
import time
import threading
from httpfsLogger import *

class httpfsServer:

    __logger = None
    __port = None
    __path = None
    __socket = None
    
    def __init__(self, verbose, port, path):
        self.__logger = ConsoleLogger(verbose)
        self.__port = port
        self.__path = path

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.start()


    def start(self):
        try:
            self.__socket.bind(('', self.__port))
            self.__socket.listen(5)
            log("Httpfs server is listening at {0}".format(self.__port))

            while True:
                connection, address = self.__socket.accept()
                threading.Thread(target=handleClient, args=(connection, address)).start()
            
        finally:
            log("Something went wrong")
            self.__socket.close()


    def handleClient(connection, address):
        log("Got a client from {0}".format(address))

        log("Closing connection from {0}".format(address))
        connection.close()
        

    def __getMessage(self):
        message = ""
        lastPacket = time.time()

        timeout = 5
        self.__socket.setttimeout(timeout)

        while True:
            if time.time() - lastPacket > timeout:
                break

            try:
                packet = self.__socket.recv(2048)
                if packet:
                    message += packet.decode("utf-8")
                    lastPacket = time.time()

            except:
                pass

        return message
            
    def log(message):
        self.__logger.displayMessage(message)
