from volatileApp.Browser import Browser
from volatileAppWin.WinApplication import WinApplication 

class Firefox(WinApplication, Browser):
    '''
    An specialized class for Browser Applications
    Extends the Application Class
    '''
    def __init__(self):
        '''
        creates a new Browser Object
        '''

        WinApplication.__init__(self, "Firefox")
    
    def windowClass(self):
        return "MozillaWindowClass"
