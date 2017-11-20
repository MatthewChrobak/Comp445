import libs
from Packet import *

pkt = Packet(PACKET_TYPE_DATA, 1, "localhost", 80, "")

print(pkt.getBytes())
