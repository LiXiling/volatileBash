# -*- coding: utf-8 -*-

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

    def _createFile(self, filename=None):
        '''
        internal function for creating a new empty file on the system
        '''

        if not filename:
            filename = self.FILENAME
            
        filePath = self.dirPath + '/' + filename
        
        if not os.path.exists(os.path.dirname(filePath)):
            os.makedirs(os.path.dirname(filePath))

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
        return self
        