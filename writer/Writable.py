# -*- coding: utf-8 -*-

import abc

class Writable(object):
    
    """A Writable is any kind of object that can be used by a Scripter to generate a script."""
    
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.solutionLines = []
        
    def addSolutionLine(self, line):
        """Adds a line to the solution text."""
        self.solutionLines.append(line)
   
    def solutionInfo(self):
        """Returns:
            str: a string containing information on data that can be 
                found in the dump and how to retrieve it.
        """
        if (len(self.solutionLines) == 0):
            return "No solution info specified for " + self.__class__.__name__
        else:
            return "\n".join(self.solutionLines)
     
    @abc.abstractmethod
    def toString(self):
        """Returns: 
            str: a ready-to-execute commandline string for scripting
        """
        pass

    def __str__(self):
        return self.toString()
    