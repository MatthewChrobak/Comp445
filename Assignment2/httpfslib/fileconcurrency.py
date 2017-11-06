from threading import Lock

writers = {}
readers = {}
lock = Lock()

def writeToFile(filepath, content):
    while (True):
        lock.acquire()
        if (canWrite(filepath)):
            addWriter(filepath)

            with open(filepath, "w") as fs:
                fs.write(content)
                
            removeWriter(filepath)
            lock.release()
        else:
            lock.release()
            time.sleep(0)

def readFromFile(filepath):
    content = ""
    
    while (True):
        lock.acquire()
        if (canRead(filepath)):
            addReader(filepath)

            with open(filepath, "r") as fs:
                content = fs.read()
            
            removeReader(filepath)
            lock.release()
        else:
            lock.release()
            time.sleep(0)

    return content

def addWriter(filename):
    writers[filename] = getNumWriters(filename) + 1

def removeWriter(filename):
    writers[filename] = getNumWriters(filename) - 1

    if writers[filename] is 0:
        del writers[filename]

def getNumWriters(filename):
    return writers.get(filename, 0)

def canWrite(filename):
    return getNumWriters(filename) is 0 and getNumReaders(filename) is 0


def addReader(filename):
    readers[filename] = getNumReaders(filename) + 1

def removeReader(filename):
    readers[filename] = getNumWriters(filename) - 1

    if readers[filename] is 0:
        del readers[filename]

def getNumReaders(filename):
    return readers.get(filename, 0)

def canRead(filename):
    return getNumWriters(filename) is 0

