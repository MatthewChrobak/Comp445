import re
import os
from httpResponse import *

class requestHandler:

    __method = None
    __filePath = None
    __headers = None
    __fileContent = None
    __path = None
    __response = None
    
    def __init__(self, args, path):
        regex = r"(POST|GET)\s+(.+)HTTP"
        match = re.search(regex, args)

        if not match:
            raise LookupError("invalid http request")


        self.__method = match.group(1)
        self.__filePath = match.group(2)
        self.__path = path


        if(self.__method == "GET"):
            self.__response = self.getFile(self.__filePath)

        if(self.__method == "POST"):
            self.__response = self.postFile(self.__filePath, self.__fileContent)


    def getFile(self, filePath):
        response = HttpResponse()
        response.setStatus(200, "OK")

        fullFilePath = os.path.realpath(self.__path + filePath)

        if (len(fullFilePath) < len(self.__path)):
            response.setStatus(401, "Unauthorized")
        else:
            if (os.path.isdir(fullFilePath)):
                response.setBody(os.listdir(fullFilePath))
            else:

                if (not os.path.isfile(fullFilePath)):
                    response.setStatus(404, "File not found")
                else:
                    with open(fullFilePath, 'r') as file:
                        fcontent = file.read()
                        response.setBody(fcontent)

        return response

    def postFile(self, filePath, fileContent):

        fullFilePath = self.__path + filePath

        if (fullFilePath is not os.path.realpath(fullFilePath)):
            return "Error 401: Unauthorized"

        fs = open(fullFilePath, "w")
        fs.write(fileContent)
        fs.close()

    def getResponse(self):
        return self.__response
