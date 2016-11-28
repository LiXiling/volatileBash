from Application import Application


class Browser(Application):
    def __init__(self, useChrome=False):
        if useChrome:
            super(Browser, self).__init__("chrome")
        else:
            super(Browser, self).__init__("firefox")


    def visitPage(self, url):
        self.addArg(url)
        return self

    def googleSearch(self, keyword):
        self.addArg("google.de/#q=" + keyword)
        return self