from libs import *

from ReceiverController import *

rc = ReceiverController(80)

while(True):
    message = rc.getMessage()
    print (message)
