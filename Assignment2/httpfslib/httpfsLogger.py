class ConsoleLogger:
    __verbose = None

    def __init__(self, verbose):
        self.__verbose = verbose

    def displayMessage(self, message):
        if (self.__verbose):
            print(message)
