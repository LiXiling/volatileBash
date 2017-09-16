# -*- coding: utf-8 -*-

from writer.app.ImageViewer import WinImageViewer
from writer.Scripter import AutoItScriptWriter
from util.Secret import Secret

"""
Szenario: Bild in Bildbetrachter geoeffnet, extrahierbar z.B. ueber Analyse
der RAW-Daten mit Gimp. Dazu benoetigt es die Breite der Bildschirmaufloesung,
welche sich erraten laesst.
Einschaetzung: 4/5, 2/5 falls das Bild mit FileCarver auffindbar ist
"""

filename = "secret.png"
imageviewer = WinImageViewer().openFile(filename).setWindowTitle(filename + ' - 400x102').setWindowDimensions(400, 102)
writer = AutoItScriptWriter()
writer.add(imageviewer).flush().writeSolutionInfo()
Secret().saveImage(writer.dirPath+filename)

