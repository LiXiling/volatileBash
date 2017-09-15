# -*- coding: utf-8 -*-

import abc

class Writable(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def toString(self):
        '''
       :return: a ready-to-execute commandline string for scripting
       '''
        pass

    def __str__(self):
        return self.toString()
    
    def solutionInfo(self):
        return "No solution info specified for " + self.__class__.__name__