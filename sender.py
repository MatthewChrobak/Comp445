

class Test:
        __callback = None

        def __init__(self, callback):
                self.__callback = callback

        def foo(self):
                self.__callback();



def printstuff():
        print("Foo")

x = Test(printstuff)
x.foo()



import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while (True):
        soc.sendto("Hello world!".encode("utf-8"), ("127.0.0.1", 80))
