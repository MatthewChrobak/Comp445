from httpRequestLine import *
from uri import *
import re

class RequestBuilder(HttpRequestLine):

    __verbose = False

    def __init__(self, args):
        regex = r"(httpc)\s+(post|get)\s+(-v\s+)?(-h\s+(\S+)\s+)*(-d\s+)?(-f\s+(\S+)\s+)?(.+)"
        match = re.search(regex, args)

        if not match:
            raise LookupError("Unable to format")
        
        httpc = match.group(1)
        method = match.group(2)
        verbose = match.group(3)
        header = match.group(4)
        headerData = match.group(5)
        data = match.group(6)
        file = match.group(7)
        filePath = match.group(8)
        dataStr = match.group(9)

        self.setRequestType(method)
        self.setURI(dataStr)


    def buildRequest(self):

        uri = Uri(self.getURI())

        # Ensure that we can actually build a request.
        if not uri.isValidURI():
            return None

        # Method SP Request-URI SP HTTP-Version CRLF
        # https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html
        requestLine = "{0} {1} {2}/{3}\r\n".format(self.getRequestType(), uri.getResourcePath(), uri.getApplicationType(), self.getHttpVersion())
        
        # Make sure we have the host.
        self.addHeader("host", uri.getDomain())
        fullRequest = "{0}\r\n{1}\r\n\r\n{2}".format(requestLine, self.getHeaders(), self.getBody())

        data = fullRequest.format("utf-8")
        self.reset()
        return data