# -*- coding: utf-8 -*-

import abc
from ..Writable import Writable

class Application(Writable):
    __metaclass__ = abc.ABCMeta
    
    '''
    A base class to model basic Applications.
    Implements Writable
    '''

    def __init__(self, cmd):
        '''
        creates a new Application Object
        :param cmd: the commandline command for this application
        '''
        Writable.__init__(self)
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
        script = 'local $pid = ShellExecute("{}", "{}")\nlocal $hWnd = WinWaitActive("{}", "")\n'\
                'Sleep(2000)'\
                .format(self.cmd, self._buildArgString(), self.windowClassString())
        if hasattr(self, 'windowTitle'):
            script += '\nWinSetTitle($hWnd, "", "' + self.windowTitle + '")'
        if hasattr(self, 'windowDimensions'):
            script += '\nWinMove($hWnd, "", Default, Default, {}, {})'.format(*self.windowDimensions)
        return script
        
    def windowClassString(self):
        return "[CLASS:{}]".format(self.windowClass())
    
    @abc.abstractmethod
    def windowClass(self):
        pass
    
    def setWindowTitle(self, string):
        self.windowTitle = string
        self.addSolutionLine('Window title of {} set to: {}. This can be found with '\
                             '"screenshot" or "windows".'\
                             .format(self.cmd, self.windowTitle))
        return self
    
    def setWindowDimensions(self, width, height):
        self.windowDimensions = (width, height)
        return self
                
    
class CMDApplication(Application):
    
    def __init__(self):
        Application.__init__(self, "cmd")
        self.commands = []
    
    def toString(self):
        return '\n'.join([Application.toString(self)] + list(map(self.sendCommand, self.commands)))
    
    def sendCommand(self, commandString):
        return 'Send("{}{{ENTER}}")'.format(commandString)
    
    def add(self, writable):
        command = '{} {}'.format(writable.cmd, writable._buildArgString())
        self.commands.append(command)
        self.addSolutionLine('The command "{}" has been executed in a cmd console. '\
                             'To see the command one can use "cmdscan".'.format(command))
        return self
    
    def windowClass(self):
        return "ConsoleWindowClass"
    