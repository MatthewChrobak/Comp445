import socket
import time
import re

class HttpcRequest:

	__httpMessage = None
	__connection = None
	__verbose = False
	__outputfilepath = None

	def __init__(self, host, port, message, verbose = False, outputfilepath = None):
		self.__connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		self.__connection.connect((host, port))
		self.__httpMessage = message

		self.__verbose = verbose
		self.__outputfilepath = outputfilepath

	def execute(self):
		self.__connection.send(self.__httpMessage.encode("utf-8"))

	def getResponse(self):
		message = self.__getMessage()
		
		splitMessage = message.split("\r\n\r\n")


		header = splitMessage[0]
		body = "\r\n".join(splitMessage[1:])

		regex = r"HTTP\/1.1\s30[012]"
		match = re.search(regex, header)

		if match:
		    regex = r"Location: (.+)"
		    match = re.search(regex, header)

		    newArgs = match.group(1)
		    return newArgs


		if self.__verbose:
			print(header)
			print("\r\n")
		print(body)

		if self.__outputfilepath is not None:
			fs = open(self.__outputfilepath, "w")
			fs.write(header)
			fs.write('\r\n')
			fs.write(body)
			fs.close()

		self.__connection.close()

		return None


	def __getMessage(self):
		message = ""
		lastPacket = time.time()

		timeout = 5
		self.__connection.settimeout(timeout)

		while True:

			if time.time() - lastPacket > timeout:
				break

			try:
				packet = self.__connection.recv(2048)
				if packet:
					message += packet.decode("utf-8")
					lastPacket = time.time()

			except:
				pass
			
		return message
