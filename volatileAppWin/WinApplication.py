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
        parts = ["local $pid = ShellExecute(\"", self.cmd, "\", \"", 
                    self._buildArgString(), "\")\n", "WinWaitActive(\"",
                    self.windowClass(), "\", \"\", 10)"]
        return "".join(parts)
    
    def windowClassString(self):
        return "".join(["[CLASS:", self.windowClass(),"]"])
    
    def windowClass(self):
        return ""