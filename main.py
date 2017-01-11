import os
import shutil

from volatileApp import Editor
from volatileApp.Browser import Browser
from volatileIO.EMLWriter import EMLWriter
from volatileIO.Scripter import Scripter

outDir = "./output/"

if os.path.exists(outDir):
    shutil.rmtree(outDir)

firefox = Browser().googleSearch("sha256")
gedit = Editor.Gedit().openFile("./main.sh")
vim = Editor.Vim().openFile("./test.eml")

script = (
    Scripter(outDir, True)
        .add(firefox)
        .add(gedit)
        .add(vim)
        .flush()
)

email = (
    EMLWriter(outDir, "test.eml")
        .flush()
)
