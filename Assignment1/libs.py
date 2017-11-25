import sys
import os

# Append the httpclib path to the module probing collection.
cwd = os.getcwd()
sys.path.append(cwd + "/httpclib/")
sys.path.append(cwd + "/../Assignment3/Sender/")
sys.path.append(cwd + "/../Assignment3/Receiver/")
sys.path.append(cwd + "/../Assignment3/Shared/")
