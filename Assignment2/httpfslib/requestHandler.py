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

        if (filePath == "/"):
            return os.listdir(self.__path)
        elif (os.path.isdir(self.__path + filePath)):
            return os.listdir(self.__path + filePath)

        fullFilePath = self.__path + filePath
        if (os.path.isfile(fullFilePath)):
            if("file out of range"):
                return "Error 401: Unauthorized"

            with open(fullFilePath, 'r') as file:
                fcontent = file.read()
                return fcontent
        else:
            return "Error 404: Not Found"

    def postFile(self, filePath, fileContent):

        fullFilePath = self.__path + filePath

        fs = open(fullFilePath, "w")
        fs.write(fileContent)
        fs.close()
