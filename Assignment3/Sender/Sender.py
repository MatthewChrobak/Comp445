import libs
from socket import *
from SenderController import *

sc = SenderController("localhost", 80)
sc.sendMessage("x" * 2027)
