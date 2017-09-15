# -*- coding: utf-8 -*-

from .Application import Application 

class Netcat(Application):
   
    def __init__(self):
        Application.__init__(self, "nc")
    
    def listen(self, port=42042):
        self.addArg("-l -p")
        self.addArg(port)
        
    def sendFileContents(self, filename, host="127.0.0.1", port=42042):
        self.addArg("-i 2")
        self.addArg(host)
        self.addArg(port)
        self.addArg("<")
        self.addArg(filename)
        
    def windowClass(self):
        return "ConsoleWindowClass"

