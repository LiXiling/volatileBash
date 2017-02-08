import os
import shutil

from volatileCrypto import RotCipher
from volatileApp import Editor
from volatileApp.Browser import Browser
from volatileIO.EMLWriter import EMLWriter
from volatileIO.Scripter import Scripter

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
        .setContent(RotCipher.enc(secretMessage, 15))
        .flush()
)

print RotCipher.enc(
    "S~ }~[34m<83>[m {t[34m<83>[m p}[34m<88>[m~}t z}~[34m<86>[m;[34m<83>[mwt U{pv x[34m<82>[m wt[34m<81>[mqp{ctpCA", -15)