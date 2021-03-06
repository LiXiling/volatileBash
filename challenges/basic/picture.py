# -*- coding: utf-8 -*-

"""
Szenario: Bild in Bildbetrachter geoeffnet, extrahierbar z.B. ueber Analyse
der RAW-Daten mit Gimp. Dazu benoetigt es die Breite der Bildschirmaufloesung,
welche sich erraten laesst.
Einschaetzung: 4/5, 2/5 falls das Bild mit FileCarver auffindbar ist
"""

##########################
# imports                #
##########################

from writer.app.ImageViewer import IrfanView
from writer.app.Application import Remove
from writer.Scripter import AutoItScriptWriter
from util.Secret import Secret

##########################
# setup writer           #
##########################

writer = AutoItScriptWriter()

##########################
# generate secrets       #
##########################

filename = "secret.png"
Secret().saveImage(writer.dirPath, filename)

##########################
# setup applications     #
##########################

imageviewer = IrfanView().openFile(filename).setWindowTitle(filename + ' - 400x102')

##########################
# applications to writer #
##########################

writer.add(imageviewer).add(Remove(filename))

##########################
# generate script        #
##########################

writer.flush().writeSolutionInfo()

