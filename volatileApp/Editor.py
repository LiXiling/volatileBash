from Application import Application

class Editor(Application):
    def openFile(self, filePath):
        self.addArg(filePath)

        return self

class Gedit(Editor):
    def __init__(self):
        super(Gedit, self).__init__("gedit")


#TODO: Open a new Terminal works, but also needs to open in this location
class Vim(Editor):
    def __init__(self):
        super(Vim, self).__init__("terminal -x sh -c\"vi")
        self.endCommand = "; bash\""

    def toString(self):
        return self.cmd + self._buildArgString() + self.endCommand