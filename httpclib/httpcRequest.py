import socket

class HttpcRequest:

	__httpMessage = None
	__connection = None
	__verbose = False
	__filepath = None

	def __init__(self, host, port, message, verbose = False, filepath = None):
		self.__connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.__connection.connect((host, port))
		self.__httpMessage = message
		self.__verbose = verbose
		self.__filepath = filepath

	def execute(self):
		self.__connection.send(self.__httpMessage.encode("utf-8"))

	def getResponse(self):
		message = self.__getMessage().split("\r\n")
		header = message[0]
		body = message[1:]
		if self.__verbose:
			print(header)
		print("\r\n")
		print(body)

		if self.__filepath is not None:
			with open(self.__filepath, "w") as fs:
				fs.write(message)

		self.__connection.close()



	def __getMessage(self):
		message = ""
		while True:
			packet = self.__connection.recv(1024, socket.MSG_WAITALL).decode("utf-8")
			message += packet
			if len(packet) < 1024:
				break
		return message


obj = HttpcRequest("google.ca", 80, "GET / HTTP/1.1\r\nHost: www.google.ca\r\n\r\n".encode("utf-8"))
obj.execute()
print(obj.getResponse())