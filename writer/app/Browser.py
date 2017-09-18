# -*- coding: utf-8 -*-

from .Application import Application

class Browser(Application):
    '''
    A specialized class for Browser Applications
    Extends the Application Class
    '''

    def openURL(self, url):
        '''
        opens the specific url on the browser
        :param url: the url to be visited
        :return: the Browser object for method chaining
        '''
        self.addArg(url)
        return self

    def googleSearch(self, searchString):
        '''
        an abstraction for using google-search
        :param keyword: the phrase to be searched for
        :return: the Browser object itself for method chaining
        '''
        searchString = searchString.replace(" ", "+")
        self.addArg("www.google.de/#q=" + searchString)
        return self


class Firefox(Browser):

    def __init__(self):
        '''
        creates a new Browser Object
        '''

        Application.__init__(self, "Firefox")
    
    def windowClass(self):
        return "MozillaWindowClass"

class InternetExplorer(Browser):
    
    def __init__(self):
        Application.__init__(self, "Iexplore")
        
    def windowClass(self):
        return "IEFrame"
    