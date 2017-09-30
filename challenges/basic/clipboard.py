# -*- coding: utf-8 -*-S

"""
Szenario: Es ist ein Textfile geoeffnet, indem sich das Flag offensichtlich
befinden muesste, doch es wurde anscheinend entfernt. Das Secret befindet sich 
im Clipboard.
Einschaetzung: 2/5
"""

##########################
# imports                #
##########################

from writer.AuxWriter import ClipboardWriter
from writer.EMLWriter import EMLWriter
from writer.Scripter import AutoItScriptWriter
from writer.app.Editor import Notepad
from util.Secret import Secret, PasswordSecret

##########################
# setup writer           #
##########################

writer = AutoItScriptWriter()

##########################
# generate secrets       #
##########################

filename = 'password.eml'
content = "Eve! Don't let anyone know that the secret passphrase is .\n" \
        "Just copy it in the login form and delete it afterwards. Don't want somebody to find it.\n"\
        "xoxo, Alice"
EMLWriter(writer.dirPath, filename, content = content).flush()
passwordSecret = str(PasswordSecret())
Secret().saveZip(writer.extraDirPath, 'secret.zip', passwordSecret)

##########################
# setup applications     #
##########################

notepad = Notepad().openFile(filename)
clipboard = ClipboardWriter().put(passwordSecret)

##########################
# applications to writer #
##########################

writer.add(clipboard).add(notepad)

##########################
# generate script        #
##########################

writer.flush().writeSolutionInfo()
