import re
import os

class requestHandler:

    __method = None
    __filePath = None
    __headers = None
    __fileContent = None
    __path = None
    
    def __init__(self, args, path):
        regex = r"(POST|GET)\s+(.+)HTTP(\/\d\.\d\\r\\n)(Content-Type:.+)(\\r\\n\\r\\n)(.+)"
        match = re.search(regex, args)

        if not match:
            raise LookupError("invalid http request")


        __method = match.group(1)
        __filePath = match.group(2)
        __headers = match.group(4)
        __fileContent = match.group(6)
        __path = path

        if(method == "GET"):
            getFile(__filePath)

        if(method == "POST"):
            postFile(__filePath, __fileContent)


    def getFile(self, filePath):

        fullFilePath = self.__path + filePath

        if (fullFilePath is not os.path.realpath(fullFilePath)):
            return "Error 401: Unauthorized"
        
        if (os.path.isdir(fullFilePath)):
            return os.listdir(fullFilePath)
        else:
            if (not os.path.isfile(fullFilePath)):
                return "Error 404: Not Found"
            else:
                with open(fullFilePath, 'r') as file:
                    fcontent = file.read()
                    return fcontent

    def postFile(self, filePath, fileContent):

        fullFilePath = self.__path + filePath

        if (fullFilePath is not os.path.realpath(fullFilePath)):
            return "Error 401: Unauthorized"

        fs = open(fullFilePath, "w")
        fs.write(fileContent)
        fs.close()
