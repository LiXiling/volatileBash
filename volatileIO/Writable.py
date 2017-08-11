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


class Comment(Writable):
    def __init__(self, str):
        self.str = str

    def toString(self):
        return '#' + self.str + '\n'


class ParalellAnd(Writable):
    def toString(self):
        return ' & '

class SequentialAnd(Writable):
    def toString(self):
        return ' && '

class XOr(Writable):
    def toString(self):
        return ' || '
