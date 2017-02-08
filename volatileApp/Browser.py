from Application import Application


class Browser(Application):
    '''
    An specialized class for Browser Applications
    Extends the Application Class
    '''
    def __init__(self):
        '''
        creates a new Browser Object
        :param useChrome: default=False. If True, will use Firefox, else Chrome
        '''

        super(Browser, self).__init__("sensible-browser")

    def visitPage(self, url):
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
        self.addArg("google.de/#q=" + searchString)
        return self
