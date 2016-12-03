import os
import abc

class FileCreator(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, filePath):
        self.filePath = filePath

    def _createFile(self):

        dir = os.path.dirname(self.filePath)

        if not os.path.exists(dir):
            os.makedirs(dir)

        f = open(self.filePath, 'w')
        f.close()

    @abc.abstractmethod
    def getContent(self):
        pass

    @abc.abstractmethod
    def flush(self):
        pass