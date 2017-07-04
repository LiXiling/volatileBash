from volatileApp.Editor import Editor
from volatileAppWin.WinApplication import WinApplication 

class Notepad(Editor, WinApplication):
    '''
    Class modeling the Notepad Editor
    '''
    def __init__(self):
        super(Notepad, self).__init__("Notepad")
        
    def windowClass(self):
        return "Notepad"

