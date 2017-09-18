# -*- coding: utf-8 -*-

import abc
import os
import shutil
import string
import random

from writer.FileCreator import FileCreator

class AbstractScripter(FileCreator): 
    
    def __init__(self, dirPath):
        FileCreator.__init__(self, dirPath)
        self.writables = []
    
    @abc.abstractmethod
    def add(self, writable):
        pass

    def _addWritable(self, writable):
        self.writables.append(writable)
        
    def getWritables(self):
        return self.writables

class AutoItScriptWriter(AbstractScripter):
    FILENAME = 'main.au3'
    
    def __init__(self, dirPath="./output", signalFilePath="signal"):
        if os.path.exists(dirPath):
            shutil.rmtree(dirPath)
        AbstractScripter.__init__(self, dirPath)
        self.signalFilePath = signalFilePath
        self.extraDirPath = dirPath + '/extra'
        
    def add(self, writable):
        self._addWritable(writable)
        return self
    
    def noise(self, length=1024):
        return ';' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
        
    def getFileContent(self):
        # Add Noise to make the file big enough to not be stored in the MFT table
        return "\n".join([self.noise(), 
            ';This script was automatically generated by volatileBash',
            'FileDelete("{}")'.format(self.signalFilePath)] +
            [str(w) for w in self.getWritables()] +
            ['FileDelete("./*")',
            'FileWrite("{}","")'.format(self.signalFilePath), 
             ])
        
    def writeSolutionInfo(self, filename="solutionInfo.txt"):
        with open(self._createFile('extra/' + filename), 'a') as f:
            for w in self.writables:
                f.write(w.solutionInfo())
        return self