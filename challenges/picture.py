import os
import shutil

from volatileAppWin.WinBrowser import Firefox
from volatileIO.AutoItScriptWriter import AutoItScriptWriter
from volutil.Secret import Secret

outDir = "./output/"

if os.path.exists(outDir):
    shutil.rmtree(outDir)

"""
Szenario: Bild in Bildbetrachter geöffnet, extrahierbar z.B. über Analyse
der RAW-Daten mit Gimp, Bilddimensionen daher im Fenstertitel
Einschätzung: 4/5, 2/5 falls das Bild mit FileCarver auffindbar ist
"""

filename = "picture.png"
firefox = Firefox().openURL(filename).setWindowTitle(Secret('out.png - 400x102').obfuscate()).setWindowDimensions(400, 102)
AutoItScriptWriter(outDir).add(firefox).flush()
Secret().saveImage(outDir+filename)

