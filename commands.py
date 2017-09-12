def ProcessInput(args):

    # Make sure we have some input.
    if (len(args) == 0):
        print("Arguments are empty.")
        return
    
    # Require that the first command be a httpc command.
    if (args[0] != "httpc"):
        print (args[0] + " is not a known command.")
        return

    # Process the httpc command.
    ProcessCommand(args)
    

def ProcessCommand(args):

    # Do we have a command to process?
    if (len(args) == 1):
        print("No argument given.")
        return

    if (args[1] == "help"):
        ProcessHelp(args)
        return

    #if (args[1] == "get"):
        # TODO
        
    #if (args[1] == "post"):
        # TODO

    print (args[1] + " is not a known httpc command.")

def ProcessHelp(args):

    # Do we need to print a simple help screen.
    if (len(args) == 2):
        print("""
httpc is a curl-like application but supports HTTP protocol only.
Usage:
    httpc command [arguments]
The commands are
    get     executes a HTTP GET request and prints the response.
    post    executes a HTTP POST request and prints the response.
    help    prints this screen.""")
    else:
        # We have 3 or more arguments. Figure out which one we want help with.
        if (args[2] == "get"):
            print("""
usage: httpc get [-v] [-h key:value] URL

Get executes a HTTP GET request for a given URL.

    -v             Prints the detail of the response such as protocol, status, and headers.
    -h  key:value  Associates headers to HTTP Request with the format 'key:value'.
""")
        elif (args[2] == "post"):
            print("""
usage: httpc post [-v] [-h key:value] [-d inline-data] [-f file] URL

Post executes a HTTP POST request for a given URL with inline data or from file.
    -v             Prints the detail of the response such as protocol, status, and headers.
    -h  key:value  Associates headers to HTTP Request with the format 'key:value'.
    -d  string     Associates an inline data to the body HTTP POST request.
    -f  file       Associates the content of a file to the body HTTP POST request.
    
Either [-d] or [-f] can be used but not both.""")
        else:
            print(args[2] + " is not a known httpc command.")     
