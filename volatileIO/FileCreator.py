import abc
import os


class FileCreator(object):
    '''
    Abstract base class for classes creating files
    '''
    __metaclass__ = abc.ABCMeta

    def __init__(self, dirPath):
        '''
        creates a new FileCreator
        :param filePath: the path to the output file
        '''
        self.dirPath = dirPath

    def _createFile(self, fileName):

        '''
        internal function for creating a new empty file on the system
        :param filePath: optional parameter - the path to the output file
                         if None, the path given by Object creation is used
        '''

        if not os.path.exists(self.dirPath):
            os.makedirs(self.dirPath)

        filePath = self.dirPath + '/' + fileName

        f = open(filePath, 'w')
        f.close()

    @abc.abstractmethod
    def getFileContent(self):
        '''
        abstract method. returns the content of the modeled File
        :return: a string representation of the File's content
        '''
        pass

    @abc.abstractmethod
    def flush(self):
        '''
        writes the File onto the system
        :return: None
        '''
        pass
