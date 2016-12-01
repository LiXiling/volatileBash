from volatileIO.Writable import Writable

class Application(Writable):
    def __init__(self, cmd):
        self.cmd = cmd
        self.args = []

    def addArg(self, arg):
        self.args.append(arg)
        return self

    def _buildArgString(self):
        string = ""
        for arg in self.args:
            string += " " + arg

        return string

    def toString(self):
        return self.cmd + self._buildArgString()