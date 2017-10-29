class HttpRequest:

    __httpVersion = "1.1"    # 1.1 by default
    __statusMessage = ""
    __responseHeaders = {}
    __responseBody = ""

    def __init__(self):
        self.reset()

    def reset(self):
        self.__httpVersion = "1.1"
        self.__responseHeaders = {}
        self.__responseBody = ""


    def addHeader(self, key, value):
        # Updates the entry if it exists, adds if it doesn't.
        self.__responseHeaders.update({str(key): str(value)})

    def getHeaders(self):
        output = ""

        for key in self.__responseHeaders.keys():
            output += "{0}: {1}\r\n".format(key, self.__responseHeaders.get(key))

        return output

    def setHttpVersion(self, version):
        print("Unable to change the HTTP version to {0} - keeping the previous version of {1}".format(version, self.__httpVersion))

    def getHttpVersion(self):
        return self.__httpVersion

    def setBody(self, body):
        self.__responseBody = body

    def getBody(self):
        return self.__responseBody

    def setStatusMessage(self, code, reason):
        self.__statusMessage = "{0} {1}".format(code, reason)

    def getStatusMessage(self):
        return self.__statusMessage

    def getFullHttpRequest(self):
        return "HTTP/{0} {1}\r\n{2}\r\n{3}".format(self.getHttpVersion(), self.getStatusMessage(), self.getHeaders(), self.getBody())
