from Application import *

class Editor(Application):
    def openFile(self, filePath):
        self.addArg(filePath)

        return self

class Gedit(Editor):
    def __init__(self):
        super(Gedit, self).__init__("gedit")

class Vim(Editor,TerminalApplication):
    def __init__(self):
        super(Vim, self).__init__("vi")