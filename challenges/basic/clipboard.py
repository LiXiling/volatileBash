# -*- coding: utf-8 -*-S

from writer.AuxWriter import ClipboardWriter
from writer.EMLWriter import EMLWriter
from writer.Scripter import AutoItScriptWriter
from writer.app.Editor import Notepad
from util.Secret import Secret

"""
Szenario: Es ist ein Textfile geoeffnet, indem sich das Flag offensichtlich
befinden muesste, doch es wurde anscheinend entfernt. Das Secret befindet sich 
im Clipboard.
Einschaetzung: 2/5
"""

filename = 'password.eml'
content = "Eve! Don't let anyone know that the secret passphrase is .\n" \
        "Just copy it in the login form and delete it afterwards. Don't want somebody to find it.\n"\
        "xoxo, Alice"
passwordSecret = str(Secret(password=True))
notepad = Notepad().openFile(filename)
clipboard = ClipboardWriter().put(passwordSecret)
writer = AutoItScriptWriter()
writer.add(clipboard).add(notepad).flush().writeSolutionInfo()
EMLWriter(writer.dirPath, filename, content = content).flush()
Secret().saveZip(writer.extraDirPath, 'secret.zip', passwordSecret)