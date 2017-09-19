# -*- coding: utf-8 -*-

import abc

class Writable(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.solutionLines = []
        
    def addSolutionLine(self, line):
        self.solutionLines.append(line)
   
    def solutionInfo(self):
        if (len(self.solutionLines) == 0):
            return "No solution info specified for " + self.__class__.__name__
        else:
            return "\n".join(self.solutionLines)
     
    @abc.abstractmethod
    def toString(self):
        '''
       :return: a ready-to-execute commandline string for scripting
       '''
        pass

    def __str__(self):
        return self.toString()
    