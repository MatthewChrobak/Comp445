from httpRequestLine import *
from uri import *
from httpcRequest import *
import re

class RequestBuilder(HttpRequestLine):

    __verbose = False
    __filepath = None

    def __init__(self, args):
        regex = r"(httpc)\s+(post|get)\s+(-v\s+)?(-h\s+(\S+)\s+)*(-d\s+(\'.+?\')\s+)?(-f\s+(\S+)\s+)?(\'.+?\')"
        match = re.search(regex, args)

        if not match:
            raise LookupError("Unable to format args into a request line")
        
        httpc = match.group(1)
        method = match.group(2)
        isVerbose = match.group(3) is not None
        isHeader = match.group(4)

        isData = match.group(6) is not None
        dataLine = match.group(7)
        file = match.group(8)
        fileLine = match.group(9)
        url = match.group(10)

        self.setRequestType(method)
        self.setURI(url[1:-1])
        self.__verbose = isVerbose

        if isHeader:
            regex = r"-h\s+(\S+)\s+"
            headerData = re.findall(regex, args)

            for headerLine in headerData:
                header = headerLine.split(':')
                self.addHeader(header[0], header[1])

        if isData:
            self.setBody(dataLine)

        if file is not None:
            self.__filepath = filePath


    def buildRequest(self):

        uri = Uri(self.getURI())

        # Method SP Request-URI SP HTTP-Version CRLF
        # https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html
        requestLine = "{0} {1} HTTP/{2}".format(self.getRequestType(), uri.getResourcePath(), self.getHttpVersion())
        
        # Make sure we have the host.
        self.addHeader("host", uri.getDomain())
        fullRequest = "{0}\r\n{1}\r\n\r\n{2}".format(requestLine, self.getHeaders(), self.getBody())

        httpcObj = HttpcRequest(uri.getDomain(), uri.getPort(), fullRequest, self.__verbose, self.__filepath)

        self.reset()
        return httpcObj