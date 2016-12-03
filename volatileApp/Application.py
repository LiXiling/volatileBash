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

    def install(self):
        string = "sudo apt-get -y install {}".format(self.cmd)

        return string

class TerminalApplication(Application):
    def __init__(self, cmd):
        super(TerminalApplication, self).__init__(cmd)

    def toString(self):
        return "(gnome-terminal -x sh -c \"" + self.cmd + self._buildArgString() + "; bash\")"