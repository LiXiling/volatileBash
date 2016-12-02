from IPython.core.prefilter import EmacsChecker

from volatileApp.Browser import Browser
from volatileApp.Application import Application
from volatileIO.ScriptWriter import ScriptWriter
from volatileIO.EMLWriter import EMLWriter
from volatileApp import Editor
outDir = "./output/"

firefox = Browser().googleSearch("sha256")
gedit = Editor.Gedit().openFile("./script.sh")
vim = Editor.Vim().openFile("./test.eml")

script = (
    ScriptWriter(outDir + "script.sh")
        .add(firefox)
        .add(gedit)
        .add(vim) #Unfinished
        .flush()
)

email = (
    EMLWriter(outDir + "test.eml")
        .flush()
)