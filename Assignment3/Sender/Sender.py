import libs
from socket import *
from SenderController import *

sc = SenderController("localhost", 12000)
sc.sendMessage("Hello world")
