# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 18:54:10 2017

@author: Victor
"""
from volatileIO.Scripter import AbstractScripter

class AutoItScriptWriter(AbstractScripter):
    FILENAME = 'main.au3'
    
    def __init__(self, dirPath):
        AbstractScripter.__init__(self, dirPath)
        
    def add(self, writable):
        self._addWritable(writable)
        return self
        
    def getFileContent(self):
        return "\n".join([str(w) for w in self.getWritables()])