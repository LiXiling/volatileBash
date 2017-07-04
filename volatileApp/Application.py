from volatileIO.Writable import Writable


class Application(Writable):
    '''
    A base class to model basic Applications.
    Implements Writable
    '''

    def __init__(self, cmd):
        '''
        creates a new Application Object
        :param cmd: the commandline command for this application
        '''
        self.cmd = cmd
        self.args = []

    def addArg(self, arg):
        '''
        adds the argument to the Application for calling
        :param arg: the argument to be added
        :return: the Application Object for method chaining
        '''
        self.args.append(arg)
        return self

    def _buildArgString(self):
        '''
        internal function to build one string containing all arguments
        :return: one string containing all arguments
        '''
        
        return " ".join(self.args)

    def toString(self):
        return self.cmd + " " + self._buildArgString()

    def install(self):
        '''
        returns the commandline command for installing this Application with apt-get
        :return: a ready-to-execute commandline string for scripting
        '''
        string = "sudo apt-get -y install {}".format(self.cmd)

        return string


class TerminalApplication(Application):
    '''
    A specialized Application implementation used for commandline applications
    '''

    def __init__(self, cmd):
        '''
        creates a new TerminalApplication object
        :param cmd: the commandline command for this terminal application
        '''
        Application.__init__(self, cmd)

    def toString(self):
        return "(gnome-terminal -x sh -c \"" + self.cmd + self._buildArgString() + "; bash\")"
