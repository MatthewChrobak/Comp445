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

        if(self.__method == "GET"):
            self.__response = self.getFile(self.__filePath)

            # See if there's a content disposition.
            regex = r"Content-Disposition:\s*(.+)"
            match = re.search(regex, args)

            if match:
                self.__response.addHeader("Content-Disposition", match.group(1))

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
                    content = fullFilePath.split(".")[-1]
                    contentType = self.analyzeContentType(content)
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
        finally:
            return response

    def getResponse(self):
        return self.__response

    def analyzeContentType(self, content):
        switch = {
                "txt": "text/html; charset=utf-8",
                "html": "text/html; charset=utf-8",
                "jpeg": "image/" + content,
                "gif": "image/" + content,
                "png": "image/" + content,
                "ico": "image/" + content,
                "mp3": "audio/" + content,
                "acc": "audio/" + content,
                "midi": "audio/" + content,
                "mp4": "video/" + content,
                "mpeg": "video/" + content,
                "avi": "video/" + content
            }
        return switch.get(content, "application/" + content)
    
            
        
        
