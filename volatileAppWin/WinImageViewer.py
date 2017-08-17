# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 14:44:39 2017

@author: Victor
"""

from volatileAppWin.WinApplication import WinApplication
from volatileApp.ImageViewer import ImageViewer
   
class WinImageViewer(WinApplication, ImageViewer):
    
    def __init__(self):
        WinApplication.__init__(self, "Explorer")
        
    def windowClass(self):
        return "Photo_Lightweight_Viewer"