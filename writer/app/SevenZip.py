# -*- coding: utf-8 -*-

from .Application import Application 

class SevenZip(Application):
   
    def __init__(self):
        Application.__init__(self, "7z")
        
    def createZip(self, zipfilename, password, *args):
        self.addArg("a")
        self.addArg("-p"+password)
        self.addArg(zipfilename)
        self.addArg(" ".join(args))
        self.addSolutionLine('A zip with password: "{}" containing files: {} has been created.'\
                             .format(password, ", ".join(args)))
        return self
        
    def windowClass(self):
        return "FM"

