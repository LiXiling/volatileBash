from IPython.core.prefilter import EmacsChecker
from volatileApp import Editor
from volatileApp.Browser import Browser
from volatileIO.EMLWriter import EMLWriter
from volatileIO.ScriptWriter import ScriptWriter

outDir = "./output/"

firefox = Browser().googleSearch("sha256")
gedit = Editor.Gedit().openFile("./script.sh")
vim = Editor.Vim().openFile("./test.eml")

script = (
    ScriptWriter(outDir + "script.sh")
        .add(firefox)
        .add(gedit)
        .add(vim)
        .flush()
)

email = (
    EMLWriter(outDir + "test.eml")
        .flush()
)