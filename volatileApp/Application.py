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
        '''
        '''
        script = 'local $pid = ShellExecute("{}", "{}")\nlocal $hWnd = WinWaitActive("{}", "")'\
                .format(self.cmd, self._buildArgString(), self.windowClassString())
        if hasattr(self, 'windowTitle'):
            script += '\nWinSetTitle($hWnd, "", "' + self.windowTitle + '")'
        if hasattr(self, 'windowDimensions'):
            script += '\nWinMove($hWnd, "", Default, Default, {}, {})'.format(*self.windowDimensions)
        return script
        
    def windowClassString(self):
        return "".join(["[CLASS:", self.windowClass(),"]"])
    
    def windowClass(self):
        return ""
    
    def setWindowTitle(self, string):
        self.windowTitle = string
        return self
    
    def setWindowDimensions(self, width, height):
        self.windowDimensions = (width, height)
        return self
    
    def solutionInfo(self):
        return "Window title set to: " + self.windowTitle if hasattr(self, 'windowTitle') else ""
                
    
class CMDApplication(Application):
    
    def __init__(self):
        Application.__init__(self, "cmd")
        self.commands = []
    
    def toString(self):
        return '\n'.join([Application.toString(self)] + list(map(self.sendCommand, self.commands)))
    
    def sendCommand(self, commandString):
        return 'Send("{}{{ENTER}}")'.format(commandString)
    
    def add(self, writable):
        self.commands.append('{} {}'.format(writable.cmd, writable._buildArgString()))
        return self
    
    def windowClass(self):
        return "ConsoleWindowClass"
    
    def solutionInfo(self):
        return "\n".join([Application.solutionInfo(self), "The following commands have been executed in cmd:"] + self.commands)