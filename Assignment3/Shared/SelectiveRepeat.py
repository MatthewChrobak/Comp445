import time
import threading

DEFAULT_WAIT_TIME = 5


class Window:

	__gotAck = False
	__gotSyn = False
	__gotSynAck = False

	__messageCallback = None	# The function which sends back a completed frame.

	def __init__(self, messageReceivedCallback):
		print("todo")

	def handlePacketAsReceiver(self, packet):
		packetType = packet.getPacketType();

		# Are we getting a new connection?
		if (packetType == PACKET_TYPE_SYN):
			# Make sure that we haven't gotten anything first.
			if (!self.__gotSyn and !self.__gotSynAck and !self.__gotAck):
				self.__gotSyn = True
				# TODO: Make a response

				self.__gotSynAck = True

		if (packetType == PACKET_TYPE_AK):
			if (self.__gotSyn and self.__gotSynAck and !self.__gotAck):
				# TODO: 
				self.__gotAck = True

		if (packetType == PACKET_TYPE_DATA):
			if (self.__gotSyn and self.__gotSynAck and self.__gotAck):
				self.handlePacket(packet)

		


	def handlePacketAsSender(self, packet):
		

	def handlePacket(self, packet):
		
		# Figure out what kind of packet it is.
		packetType = packet.getPacketType();
		
		if (packetType == PACKET_TYPE_SYN):




	__windowAked = None		# Denotes whether or not a window frame has been received or not.
	__timers = None			# Keeps track of the last send time for a window frame.
	__timeout = DEFAULT_WAIT_TIME
	__windowStart = 0		# 

	def __init__(self, windowSize, waitTime, timeoutcallback):
		self.__windowData = [False] * windowSize
		self.__timers = time.time() * windowSize

		threading.Thread(target=self.__monitorWindow, args=(timeoutcallback).start()


	def __monitorWindow(self, timeoutcallback):
		while (True):
			for i in range(0, len(self.__windowData)):
				elapsedTime = time.time() - self.__timers[i]
				sequenceNumber = (self.__windowStart + i) % 

				if (elapsedTime >= self.__timeout):
					self.__timers[i] = time.time()
					timeoutcallback()


window.init(5);