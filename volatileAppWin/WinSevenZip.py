from volatileAppWin.WinApplication import WinApplication 

class WinSevenZip(WinApplication):
   
    def __init__(self):
        WinApplication.__init__(self, "7z")
        
    def createZip(self, zipfilename, password, *args):
        self.addArg("a")
        self.addArg("-p"+password)
        self.addArg(zipfilename)
        self.addArg(" ".join(args))
        return self
        
    def windowClass(self):
        return "FM"

