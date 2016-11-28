from volatileIO.Writable import Writable

class Application(Writable):
    def __init__(self, cmdName):
        self.cmdName = cmdName
        self.args = []

    def addArg(self, arg):
        self.args.append(arg)
        return self

    def toString(self):
        string = str(self.cmdName)

        for arg in self.args:
            string += " " + arg
        return string