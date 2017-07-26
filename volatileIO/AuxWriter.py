# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 17:24:05 2017

@author: Victor
"""
from volatileIO.Writable import Writable

class RegistryWriter(Writable):
    
    def __init__(self):
        self.lines = []
        
    def createRegistryEntry(self, key, value, path='HKEY_CURRENT_USER\Software\MaliciousApp', 
                            valuetype="REG_SZ"):
        self.lines.append("".join(['RegWrite("', path, '", "', key, '", "', 
                                             valuetype, '", "', value, '")']))
        return self
    
    def toString(self):
        return "\n".join(self.lines)
  
    
class AutoLogin(RegistryWriter):
   
    def enable(self, name, password, domain=""): 
        regPath = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon'
        self.createRegistryEntry("DefaultUserName", name, regPath)
        self.createRegistryEntry("DefaultPassword", password, regPath)
        self.createRegistryEntry("DefaultDomainName", domain, regPath)
        self.createRegistryEntry("AutoAdminLogon", "1", regPath)
        return self
    

class ClipboardWriter(Writable):
    
    def __init__(self):
        self.value = None
        
    def put(self, value):
        self.value = value
        return self
        
    def toString(self):
        return 'ClipPut("' + str(self.value) + '")'