from Application import *


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


class Gedit(Editor):
    '''
    Class modeling the Gedit Editor
    '''
    def __init__(self):
        super(Gedit, self).__init__("gedit")


class Vim(Editor, TerminalApplication):
    '''
    Class modeling the vim Editor
    '''
    def __init__(self):
        super(Vim, self).__init__("vi")
