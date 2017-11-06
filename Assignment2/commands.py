import re
import os
from httpfsServer import *

def ProcessInput(args):

    # Make sure we have some input.
    if (len(args) == 0):
        print("Arguments are empty.")
        return
    
    # Require that the first command be a httpfs command.
    if (args[0] != "httpfs"):
        print (args[0] + " is not a known command.")
        return

    # From here we can start the server and parse the input.
    CreateServer(args)

def CreateServer(args):
    regex = r"httpfs\s*(\-v)?\s*(\-p\s+(\d+))?\s*(\-d\s+(\'.+?\'))?"
    match = re.search(regex, " ".join(args))

    if not match:
        raise LookupError("Unable to format args")

    verbose = match.group(1) is not None

    port = 8080
    if match.group(2) is not None:
        port = match.group(3)
    
    path = os.getcwd()
    if match.group(4) is not None:
        path = match.group(5)

    
    httpfsServer(verbose, port, path)
