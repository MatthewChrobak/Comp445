import sys
import libs
from commands import *

while (True):
   try:
        ProcessInput(sys.stdin.readline().split())
   except BaseException as error:
        print(error)
