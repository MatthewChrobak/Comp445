import socket
import time
import threading
from httpfsLogger import *
from requestHandler import *

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
            self.__socket.bind(('', int(self.__port)))
            self.__socket.listen(5)
            self.log("Httpfs server is listening at {0}".format(self.__port))

            while True:
                connection, address = self.__socket.accept()
                threading.Thread(target=self.handleClient, args=(connection, address)).start()
            
        finally:
            self.log("Something went wrong")
            self.__socket.close()


    def handleClient(self, connection, address):
        self.log("Got a client from {0}".format(address))

        message = self.__getMessage(connection)
        print("Handling message {0}".format(message))
        response = requestHandler(message, self.__path).getResponse().getFullHttpRequest().encode("utf-8")

        print("Responding with")
        print(response)

        connection.sendall(response)

        self.log("Closing connection from {0}".format(address))
        connection.close()
        

    def __getMessage(self, connection):
        message = ""
        lastPacket = time.time()

        timeout = 5

        while True:
            if time.time() - lastPacket > timeout:
                break

            try:
                packet = connection.recv(2048)
                if packet:
                    message += packet.decode("utf-8")
                    lastPacket = time.time()

            except:
                pass

        return message
            
    def log(self, message):
        self.__logger.displayMessage(message)
