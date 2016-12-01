import os

def makeFile(filePath, firstLine=''):

    dir = os.path.dirname(filePath)

    if not os.path.exists(dir):
        os.makedirs(dir)

    f = open(filePath, 'w')
    f.write(firstLine)
    f.close()