# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 14:44:39 2017

@author: Victor
"""

from volatileApp.Application import Application

class ImageViewer(Application):
    
    def openFile(self, filePath):
        '''
        opens a file in the Editor
        :param filePath: the path to the file to be opened
        :return: the Editor object for method chaining
        '''
        self.addArg(filePath)

        return self
    
class Eog(ImageViewer):
    
    def __init__(self):
        super(Eog, self).__init__("eog")