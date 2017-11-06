from httpRequest import *
from uri import *
from httpcRequest import *
import re

class HttpcRequestBuilder(HttpRequest):

    __verbose = False
    __outputfilepath = None

    def __init__(self, args):
        regex = r"(httpc)\s+(post|get)\s+(-v\s+)?(-h\s+(\S+)\s+)*(-d\s+(\'.+?\')\s+)?(-f\s+(\'.+?\')\s+)?(-o\s+(\'.+?\')\s+)?(\'.+?\')"
        match = re.search(regex, args)

        if not match:
            raise LookupError("Unable to format args into a request line")
        
        httpc = match.group(1)
        method = match.group(2).upper()
        isVerbose = match.group(3) is not None
        isHeader = match.group(4)

        isData = match.group(6) is not None
        dataLine = match.group(7)
        if (dataLine):
            dataLine = dataLine[1:-1]

        isFile = match.group(8) is not None
        filePath = match.group(9)

        if (method == "GET" and (isFile or isData)):
            raise LookupError("Cannot use -d or -f for a GET request")

        if (isFile and isData):
            raise LookupError("Cannot use both -d and -f for a post request.")

        outputfile = match.group(10)
        outputfilePath = match.group(11)
        url = match.group(12)

        self.setRequestType(method)
        self.setURI(url[1:-1])
        self.__verbose = isVerbose

        if isHeader:
            regex = r"-h\s+(\'.+?\')\s+"
            headerData = re.findall(regex, args)

            for headerLine in headerData:
                header = headerLine[1:-1].split(':')
                self.addHeader(header[0], header[1])

        if isData:
            self.addHeader("Content-Length", len(dataLine))
            self.setBody(dataLine)

        if (isFile):
            with open(filePath[1:-1], 'r') as file:
                fcontent = file.read()
                self.addHeader("Content-Length", len(fcontent))
                self.setBody(fcontent)

        if outputfile is not None:
            self.__outputfilepath = outputfilePath[1:-1]


    def buildRequest(self):

        uri = Uri(self.getURI())

        # Method SP Request-URI SP HTTP-Version CRLF
        # https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html
        requestLine = "{0} {1} HTTP/{2}".format(self.getRequestType(), uri.getResourcePath() + uri.getArguments(), self.getHttpVersion())
        
        # Make sure we have the host.
        self.addHeader("host", uri.getDomain())
        fullRequest = "{0}\r\n{1}\r\n{2}".format(requestLine, self.getHeaders(), self.getBody())

        httpcObj = HttpcRequest(uri.getDomain(), uri.getPort(), fullRequest, self.__verbose, self.__outputfilepath)

        self.reset()
        return httpcObj
