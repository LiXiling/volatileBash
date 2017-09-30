# -*- coding: utf-8 -*-

"""
Szenario: Ein Nutzer verwendet ueberall dasselbe Passwort, welches es rauszufinden gilt.
Eine in Notepad geoeffnete Email-Datei deutet auf das Windows-Passwort hin.
Dieses laesst sich gehasht finden (volatility hashdump) und ist garantiert so schlecht,
dass es sich mit Online-Tools leicht knacken laesst. 
Einschaetzung: 4/5
"""

##########################
# imports                #
##########################

from util.Secret import Secret, PasswordSecret
from writer.AuxWriter import PasswordWriter
from writer.EMLWriter import EMLWriter
from writer.Scripter import AutoItScriptWriter
from writer.app.Editor import Notepad

##########################
# setup writer           #
##########################

writer = AutoItScriptWriter()

##########################
# generate secrets       #
##########################

filename = 'stop.eml'
content = "Eve! Stop using ur win password everywhere - bad enough I know it..\n"\
        "xoxo, Alice"
passwordSecret = str(PasswordSecret())
Secret().saveZip(writer.extraDirPath, 'secret.zip', passwordSecret)
EMLWriter(writer.dirPath, filename, content = content).flush()

##########################
# setup applications     #
##########################

notepad = Notepad().openFile(filename)
passwordWriter = PasswordWriter().setPassword(passwordSecret)

##########################
# applications to writer #
##########################

writer.add(passwordWriter).add(notepad)

##########################
# generate script        #
##########################

writer.flush().writeSolutionInfo()
