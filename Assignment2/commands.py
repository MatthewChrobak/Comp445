import re
import os

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
    regex = r""
    match = re.search(regex, args)

    verbose = False
    port = 8080
    path = os.getcwd()
