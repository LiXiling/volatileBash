from volatileApp.Application import Application, TerminalApplication


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
        Editor.__init__(self, "gedit")


class Vim(Editor, TerminalApplication):
    '''
    Class modeling the vim Editor
    '''
    def __init__(self):
        Editor.__init__(self, "vi")
