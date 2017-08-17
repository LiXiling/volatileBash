# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 17:24:05 2017

@author: Victor
"""
from volatileIO.Writable import Writable

class RegistryWriter(Writable):
    
    def __init__(self):
        self.lines = []
        self.solutionLines = []
        
    def createRegistryEntry(self, key, value, path='HKEY_CURRENT_USER\Software\MaliciousApp', 
                            valuetype="REG_SZ"):
        self.lines.append('RegWrite("{}", "{}", "{}", "{}")'.format(path, key, valuetype, value))
        self.solutionLines.append('Registry entry with key: {}, value: {} at: {}'.format(key, value, path))
        return self
    
    def toString(self):
        return "\n".join(self.lines)
    
    def solutionInfo(self):
        return "\n".join(self.solutionLines + ["Volatility commands to detect this include hivelist, printkey and lsadump"])
        
  
    
class AutoLogin(RegistryWriter):
   
    def enable(self, name, password, domain=""): 
        regPath = 'HKLM64\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon'
        self.createRegistryEntry("DefaultUserName", name, regPath)
        self.createRegistryEntry("DefaultPassword", password, regPath)
        self.createRegistryEntry("DefaultDomainName", domain, regPath)
        self.createRegistryEntry("AutoAdminLogon", "1", regPath)
        return self
    
    def solutionInfo(self):
        return 'Windows Autologon enabled:\n' + RegistryWriter.solutionInfo(self)
    

class ClipboardWriter(Writable):
    
    def __init__(self):
        self.value = None
        
    def put(self, value):
        self.value = value
        return self
        
    def toString(self):
        return 'ClipPut("' + str(self.value) + '")'
    
    def solutionInfo(self):
        return "The clipboard contains: " + str(self.value)