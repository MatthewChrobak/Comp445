import re
import os
from httpResponse import *
from fileconcurrency import *

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

        cd_startpos = args.find("Content-Disposition")
        if (cd_startpos >=0):
            cd_message = args[cd_startpos:]
            cd_endpos = cd_message.find("\r\n")
            cd_message = cd_message[:cd_endpos]
        

        if(self.__method == "GET"):
            self.__response = self.getFile(self.__filePath)

        if(self.__method == "POST"):
            self.__fileContent = args.split("\r\n\r\n")[1:][0]
            self.__response = self.postFile(self.__filePath, self.__fileContent)


    def getFile(self, filePath):
        response = HttpResponse()
        response.setStatus(200, "OK")

        fullFilePath = os.path.realpath(self.__path + filePath)

        if (not fullFilePath.startswith(self.__path)):
            response.setStatus(401, "Unauthorized")
        else:
            if (os.path.isdir(fullFilePath)):
                response.setBody(os.listdir(fullFilePath))
            else:

                if (not os.path.isfile(fullFilePath)):
                    response.setStatus(404, "File not found")
                else:
                    content = fullFilePath,split(".")[-1]
                    contentType = analyzeContentType(content)
                    response.addHeader("Content-Type", contentType)
                    with open(fullFilePath, 'r') as file:
                        fcontent = file.read()
                        response.setBody(fcontent)

        return response

    def postFile(self, filePath, fileContent):
        response = HttpResponse()
        response.setStatus(200, "OK")

        fullFilePath = os.path.realpath(self.__path + filePath)

        if (not fullFilePath.startswith(self.__path)):
            response.setStatus(401, "Unauthorized")
            return response

        try:
            writeToFile(fullFilePath, fileContent)
        except IOError:
            response.setStatus(403, "IO Error")

        return response

    def getResponse(self):
        return self.__response

    def analyzeContentType(content):
        if (content == "txt" or "html"):
            return "text/html; charset=utf-8"
        if (content == "jpeg" or "gif" or "png" or "ico"):
            return "image/" + content
        if (content == "mp3" or "acc" or "midi"):
            return "audio/" + content
        if (content == "mp4" or "mpeg" or "avi"):
            return "video/" + content
        if (content == "pdf" or "rar" or "doc" or "jar" or "js" or "json"):
            return "application/" + content
            
        
        
