# -*- coding: utf-8 -*-

from .Application import Application

class Editor(Application):
    '''
    An specialized class for Editor Applications
    Extends the Application Class
    '''
    def openFile(self, filePath):
        '''
        opens a file in the Editor
        :param filePath: the path to the file to be opened
        :return: the Editor object for method chaining
        '''
        self.addArg(filePath)

        return self

class Notepad(Editor):
    '''
    Class modeling the Notepad Editor
    '''
    def __init__(self):
        super(Notepad, self).__init__("Notepad")
        
    def windowClass(self):
        return "Notepad"
