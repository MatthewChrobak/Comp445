import re
import os

class requestHandler:

	def __init__(self, args):
		regex = r"(POST|GET)\s+(.+)HTTP"
        match = re.search(regex, args)
		
		if not match:
			raise LookupError("invalid http request")
		
		
		method = match.group(1)
		filePath = match.group(2)
		
		if(method == "GET"):
			getFile(filePath)
			
		if(method == "POST"):
			postFile(filePath)
			
	
	def getFile(self, filePath):
		
		if (filePath == "/")
			return "a list of current files"
		
		fullFilePath = os.getcwd() + filePath
		if (os.path.isfile(fullFilePath)):
			if("file out of range"):
				return "Error 401: Unauthorized"
				
			with open(fullFilePath, 'r') as file:
				fcontent = file.read()
				return fcontent
		else:
			return "Error 404: Not Found"
			
	def postFile(self, filePath, fileContent):
		
		fullFilePath = os.getcwd() + filePath
		if fullFilePath is not None:
			fs = open(fullFilePath, "w")
			fs.write(fileContent)
			fs.close()
		
		
		
		
		
		
		
	