import abc
import os


class FileCreator(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, filePath):
        self.filePath = filePath

    def _createFile(self, filePath=None):

        if filePath is None:
            filePath = self.filePath

        dir = os.path.dirname(filePath)

        if not os.path.exists(dir):
            os.makedirs(dir)

        f = open(filePath, 'w')
        f.close()

    @abc.abstractmethod
    def getContent(self):
        pass

    @abc.abstractmethod
    def flush(self):
        pass
