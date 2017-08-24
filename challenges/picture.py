from volatileApp.ImageViewer import WinImageViewer
from volatileIO.Scripter import AutoItScriptWriter
from volutil.Secret import Secret

"""
Szenario: Bild in Bildbetrachter geöffnet, extrahierbar z.B. über Analyse
der RAW-Daten mit Gimp, Bilddimensionen daher im Fenstertitel
Einschätzung: 4/5, 2/5 falls das Bild mit FileCarver auffindbar ist
"""

filename = "picture.png"
imageviewer = WinImageViewer().openFile(filename).setWindowTitle(filename + ' - 400x102').setWindowDimensions(400, 102)
writer = AutoItScriptWriter()
writer.add(imageviewer).flush().writeSolutionInfo()
Secret().saveImage(writer.dirPath+filename)

