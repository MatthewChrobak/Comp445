class HttpRequestLine:

    __requestType = None    # GET or POST - GET by default
    __httpVersion = None    # 1.1 by default
    __requestHeaders = None
    __requestBody = None
    __requestURI = None

    def __init__(self):
        self.reset()

    def reset(self):
        self.__requestType = "GET"
        self.__httpVersion = "1.1"
        self.__requestHeaders = {}
        self.__requestBody = ""
        self.__requestURI = ""


    def addHeader(self, key, value):
        # Updates the entry if it exists, adds if it doesn't.
        self.__requestHeaders.update({str(key): str(value)})

    def getHeaders(self):
        output = ""

        for key in self.__requestHeaders.keys():
            output += "{0}: {1}".format(key, self.__requestHeaders.get(key)) + "\r\n"

        return output

    def setRequestType(self, requestType):
        requestType = requestType.upper()

        if requestType == "GET" or requesetType == "POST":
            self.__requestType = requestType
        else:
            print("Unknown request type {0} - keeping the previous requeset type of {1}".format(requestType, self.__requestType))

    def getRequestType(self):
        return self.__requestType

    def setHttpVersion(self, version):
        print("Unable to change the HTTP version to {0} - keeping the previous version of {1}".format(version, self.__httpVersion))

    def getHttpVersion(self):
        return self.__httpVersion

    def setBody(self, body):
        self.__requestBody = body

    def getBody(self):
        return self.__requestBody

    def setURI(self, uri):
        self.__requestURI = uri

    def getURI(self):
        return self.__requestURI is not None