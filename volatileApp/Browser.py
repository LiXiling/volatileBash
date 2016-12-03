from Application import Application


class Browser(Application):
    '''
    An specialized class for Browser Applications
    Extends the Application Class
    '''
    def __init__(self, useChrome=False):
        '''
        creates a new Browser Object
        :param useChrome: default=False. If True, will use Firefox, else Chrome
        '''
        if useChrome:
            super(Browser, self).__init__("chrome")
        else:
            super(Browser, self).__init__("firefox")

    def visitPage(self, url):
        '''
        opens the specific url on the browser
        :param url: the url to be visited
        :return: the Browser object for method chaining
        '''
        self.addArg(url)
        return self

    def googleSearch(self, keyword):
        '''
        an abstraction for using google-search
        :param keyword: the phrase to be searched for
        :return: the Browser object itself for method chaining
        '''
        self.addArg("google.de/#q=" + keyword)
        return self
