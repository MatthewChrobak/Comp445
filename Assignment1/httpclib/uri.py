from urllib.parse import urlparse

class Uri:
    __applicationType = None
    __host = None
    __port = None
    __resourcePath = None
    __arguments = None

    def __init__(self, fullUri):
        uri = urlparse(fullUri)

        # Set the scheme first - as it might be overwritten later.
        self.__applicationType = uri.scheme + "://"

        # if the hostname and port are not defined, then it means that there was no scheme provided.
        if uri.hostname == None and uri.port == None:
            # Append it to the previous uri, and re-parse it.
            # This will force the domain and port to go to the right properties.
            # Set the application type to an empty string to hide our tracks.
            self.__applicationType = "http://"
            uri = urlparse(self.getApplicationType() + fullUri)

        self.__arguments = uri.query
        self.__resourcePath = uri.path
        if uri.path == "":
                self.__resourcePath = "/"
        self.__host = uri.hostname
        
        # Only set the port if there is one.
        if not uri.port == None:
            self.__port = uri.port
        else:
            self.__port = 80

    def getApplicationType(self):
        return self.__applicationType

    def getDomain(self):
        return self.__host

    def getResourcePath(self):
        return self.__resourcePath

    def getArguments(self):
        return self.__arguments

    def getPort(self):
        return self.__port

    def getFullURI(self):
        output = "{0}{1}{2}".format(self.__applicationType, self.getDomain(), self.getResourcePath())

        if self.__arguments is not "":
            output += "?{0}".format(self.getArguments())

        return output
