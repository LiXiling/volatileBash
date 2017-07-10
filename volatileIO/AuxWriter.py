# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 17:24:05 2017

@author: Victor
"""
from Writable import Writable

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
  
    
class ClipboardWriter(Writable):
    
    def __init__(self):
        self.value = None
        
    def put(self, value):
        self.value = value
        return self
        
    def toString(self):
        return 'ClipPut("' + str(self.value) + '")'