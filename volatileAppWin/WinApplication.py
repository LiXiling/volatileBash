# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 16:58:10 2017

@author: Victor
"""

from volatileApp.Application import Application

class WinApplication(Application):
    '''
    WinApplication creates AutoIt scripts (www.autoitscript.com) instead of
    shell scripts for execution on Windows.
    '''
    
    def __init__(self, cmd):
        '''
        creates a new WinApplication object
        :param cmd: the commandline command for this terminal application
        '''
        Application.__init__(self, cmd)
    
    def install(self):
        pass
    
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
    
class WinCMDApplication(WinApplication):
    
    def __init__(self):
        WinApplication.__init__(self, "cmd")
        self.commands = []
    
    def toString(self):
        return '\n'.join([WinApplication.toString(self)] + self.commands)
    
    def sendCommand(self, commandString):
        self.commands.append('Send("{}{{ENTER}}")'.format(commandString))
        return self
    
    def add(self, writable):
        self.sendCommand('{} {}'.format(writable.cmd, writable._buildArgString()))
        return self
    
    def windowClass(self):
        return "ConsoleWindowClass"
    