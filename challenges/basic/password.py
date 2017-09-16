# -*- coding: utf-8 -*-

from util.Secret import Secret
from writer.AuxWriter import PasswordWriter
from writer.EMLWriter import EMLWriter
from writer.Scripter import AutoItScriptWriter
from writer.app.Editor import Notepad

"""
Szenario: Ein Nutzer verwendet ueberall dasselbe Passwort, welches es rauszufinden gilt.
Eine in Notepad geoeffnete Email-Datei deutet auf das Windows-Passwort hin.
Dieses laesst sich gehasht finden (volatility hashdump) und ist garantiert so schlecht,
dass es sich mit Online-Tools leicht knacken laesst. 
Einschaetzung: 4/5
"""

filename = 'stop.eml'
content = "Eve! Stop using ur win password everywhere - bad enough I know it..\n"\
        "xoxo, Alice"
passwordSecret = str(Secret(password=True))
notepad = Notepad().openFile(filename)
writer = AutoItScriptWriter()
passwordWriter = PasswordWriter().setPassword(passwordSecret)
writer.add(passwordWriter).add(notepad).flush().writeSolutionInfo()
EMLWriter(writer.dirPath, filename, content = content, receiver = "eve@email.com").flush()
Secret().saveZip(writer.extraDirPath, 'secret.zip', passwordSecret)