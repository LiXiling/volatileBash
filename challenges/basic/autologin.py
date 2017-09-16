# -*- coding: utf-8 -*-

from writer.Scripter import AutoItScriptWriter
from writer.AuxWriter import AutoLogin
from writer.app.Browser import Firefox
from util.Secret import Secret

"""
Szenario: Ein Nutzer verwendet ueberall dasselbe Passwort, welches es rauszufinden gilt.
In Windows ist Autologin aktiviert und das Passwort laesst sich somit in der
Registry in Klartext finden (easy-mode) oder im lsadump (hard-mode, ungetestet).
Einschaetzung: 3/5 easy, 5/5 hard
"""

passwordSecret = str(Secret(password=True))
autologin = AutoLogin().enable('Eve', passwordSecret, easy=True)
firefox = Firefox().googleSearch('enable autologin windows')
writer = AutoItScriptWriter()
writer.add(autologin).add(firefox).flush().writeSolutionInfo()
Secret().saveZip(writer.extraDirPath, 'secret.zip', passwordSecret)