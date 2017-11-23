import libs
from socket import *
from SenderController import *

sc = SenderController("localhost", 80)
sc.sendMessage("Hello world")
