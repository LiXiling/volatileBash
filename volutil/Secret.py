# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 09:29:02 2017

@author: Victor
"""
import string
import random

class Secret():
    
    def __init__(self, string=None):
        self.secret = 'FLG:(' + (string if string else self._generate()) + ')'
        
    def _generate(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    
    def obfuscate(self):
        self.secret = '\x1f'.join(self.secret)
        return self
    
    def __str__(self):
        return self.secret