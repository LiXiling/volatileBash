import os
import shutil

from volatileCrypto import RotCipher
from volatileApp import Editor
from volatileApp.Browser import Browser
from volatileIO.EMLWriter import EMLWriter
from volatileIO.Scripter import Scripter
from volutil.txt2img import *

outDir = "./output/"

if os.path.exists(outDir):
    shutil.rmtree(outDir)

secretMessage = "Do not let anyone know, the Flag is herbalTea42"


firefox = Browser().googleSearch("rotation cipher base 15")

vim = Editor.Vim().openFile("./test.eml")

script = (
    Scripter(outDir, False)
        .add(firefox)
        .add(vim)
        .flush()
)

email = (
    EMLWriter(outDir, "test.eml")
        #.setContent(RotCipher.enc(secretMessage, 15))
	.setContent(secretMessage)
        .flush()
)

show(txt2img("TEST"))