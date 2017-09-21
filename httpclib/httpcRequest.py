import socket
import time

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
		message = self.__getMessage()
		splitMessage = message.split("\r\n\r\n")
		header = splitMessage[0]
		body = "\r\n".join(splitMessage[1:])
		if self.__verbose:
			print(header)
			print("\r\n")
		print(body)

		if self.__filepath is not None:
			fs = open(self.__filepath, "w")
			fs.write(header)
			fs.write('\r\n')
			fs.write(body)
			fs.close()

		self.__connection.close()



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
