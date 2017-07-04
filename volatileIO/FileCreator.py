import abc
import os


class FileCreator(object):
    '''
    Abstract base class for classes creating files
    '''
    __metaclass__ = abc.ABCMeta
    FILENAME = None

    def __init__(self, dirPath):
        '''
        creates a new FileCreator
        :param filePath: the path to the output file
        '''
        self.dirPath = dirPath

    def _createFile(self):

        '''
        internal function for creating a new empty file on the system
        '''

        if not os.path.exists(self.dirPath):
            os.makedirs(self.dirPath)

        filePath = self.dirPath + '/' + self.FILENAME

        f = open(filePath, 'w')
        f.close()

        return filePath

    @abc.abstractmethod
    def getFileContent(self):
        '''
        abstract method. returns the content of the modeled File
        :return: a string representation of the File's content
        '''
        pass

    def flush(self):
        '''
        writes the File onto the system
        :return: None
        '''
        filepath = self._createFile()

        with open(filepath, 'a') as f:
            f.write(self.getFileContent())
        