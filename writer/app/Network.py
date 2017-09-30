"""This module provides classes for networking applications."""
# -*- coding: utf-8 -*-

from .Application import Application 
 
class Netcat(Application):
    
    """Class for generating script to start netcat, a tool for network data transfer."""
    
    def __init__(self):
        Application.__init__(self, "nc", headless=True)
    
    def listen(self, port=42042):
        """Sets up netcat to listen on given port"""
        self.addArg("-k -l -p")
        self.addArg(str(port))
        self.addSolutionLine("Netcat (nc.exe) is listening on port {}. "\
                             "Volatility netscan shows active network connections."\
                             .format(port))
        return self
        
    def _addArgsForSend(self, host, port):
        self.addArg("-q 1")
        self.addArg("-i 2")
        self.addArg(str(host))
        self.addArg(str(port))
        self.addArg("<")
        
    def sendFileContents(self, filename, path='./', host="127.0.0.1", port=42042):
        """Sends the specified file to given host and port line by line."""
        self._addArgsForSend(host, port)
        self.addArg('{}/{}'.format(path, filename))
        return self
    
    def send(self, text, host="127.0.0.1", port=42042):
        self._addArgsForSend(host, port)
        self.addArg("<(echo \"{}\")".format(text))
        return self
        
    def windowClass(self):
        return "ConsoleWindowClass"


class Wireshark(Application):
    
    """Class for generating script to start Wireshark, a popular tool to capture network traffic."""
    
    def __init__(self):
        Application.__init__(self, "wireshark")
        
    def capture(self, port=42042, lastPort=None, interface=5):
        """Lets wireshark capture tcp traffic on given port and interface."""
        if lastPort:
            portFilter = "tcp portrange {}-{}".format(port, lastPort)
        else:
            portFilter = "tcp port {}".format(port)
        self.addArg("-i {}".format(interface))
        self.addArg("-f \"\"{}\"\"".format(portFilter))
        self.addArg("-k")
        self.addSolutionLine("Wireshark is capturing tcp traffic on port {}. "\
                             "The content can either be found by grep for the "\
                             "portnumber on a strings output, or by tools like "\
                             "bulk_extractor, which can get tcp packets from "\
                             "memory dumps.".format(port))
        return self
    
    def windowClass(self):
        # The window class trick runs into problems here, but so far no other app uses this class.
        return "Qt5QWindowIcon"