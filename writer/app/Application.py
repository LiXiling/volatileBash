"""This module provides classes for not-stand-alone-applications."""
# -*- coding: utf-8 -*-

import abc
from ..Writable import Writable

class Application(Writable):
    __metaclass__ = abc.ABCMeta
    
    """A base class to model basic Applications.
    Implements Writable
    """

    def __init__(self, cmd, headless=False):
        """creates a new Application Object
        Args:
            cmd (str): the commandline command for this application
            headless (bool, optional): In headless mode, the script will not wait
                for the application window to appear. Defaults to False.
        """
        Writable.__init__(self)
        self.cmd = cmd
        self.args = []
        self.headless = headless

    def addArg(self, arg):
        """Adds the argument to the Application for calling.
        Args:
            arg (str): the argument to be added
        Returns:
            Application: the Application Object for method chaining
        """
        self.args.append(arg)
        return self

    def _buildArgString(self):
        """Internal function to build one string containing all arguments."""
        return " ".join(self.args)

    def command(self):
        """
        Returns:
           str: the full command with all arguments as string 
        """
        return "{} {}".format(self.cmd, self._buildArgString())
    
    def toString(self):
        lines = ['local $pid = ShellExecute("{}", "{}")'.format(self.cmd, self._buildArgString())] 
        if not self.headless:
            lines.append('local $hWnd = WinWaitActive("{}", "")'.format(self.windowClassString()))
        lines.append('Sleep(5000)')
        if hasattr(self, 'windowTitle'):
            lines.append('WinSetTitle($hWnd, "", "{}")'.format(self.windowTitle))
        if hasattr(self, 'windowDimensions'):
            lines.append('WinMove($hWnd, "", Default, Default, {}, {})'.format(*self.windowDimensions))
        if hasattr(self, 'windowPosition'):
            lines.append('WinMove ($hWnd, "", {}, {})'.format(*self.windowPosition))
        return "\n".join(lines)
        
    def windowClassString(self):
        """Returns:
            str: a string usable by AutoIt to find the correct application window
        """
        return "[CLASS:{}]".format(self.windowClass())
    
    @abc.abstractmethod
    def windowClass(self):
        """Returns:
            str: the window class string of the applications main window.
        """
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
    
    def setWindowPosition(self, x, y):
        self.windowPosition = (x,y)
        return self
                
    
class CMDApplication(Application):
    
    """An application which can execute other applications in a CMD-Terminal"""
    
    def __init__(self):
        Application.__init__(self, "cmd")
        self.commands = []
    
    def toString(self):
        return '\n'.join([Application.toString(self)] + list(map(self.sendCommand, self.commands)))
    
    def sendCommand(self, commandString):
        """Args:
            commandString (str): the command to type
        Returns:
            An AutoIt command which auto-types the given command in the cmd terminal.
        """
        return 'Send("{}{{ENTER}}")'.format(commandString)
    
    def add(self, application):
        """Adds the given application to the list of commands to execute.
        Args:
            application (Application): an application executable in commandline
        """
        command = '{} {}'.format(application.cmd, application._buildArgString())
        self.commands.append(command)
        self.addSolutionLine('The command "{}" has been executed in a cmd console. '\
                             'To see the command one can use "cmdscan".'.format(command))
        return self
    
    def windowClass(self):
        return "ConsoleWindowClass"
    
class Remove(Writable):
    
    """Simple wrapper for the del command"""

    def __init__(self, filename):
        Writable.__init__(self)
        self.filename = filename
        
    def toString(self):
        return 'FileDelete("{}")'.format(self.filename)
