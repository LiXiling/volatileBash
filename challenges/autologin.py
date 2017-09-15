# -*- coding: utf-8 -*-

from writer.Scripter import AutoItScriptWriter
from writer.AuxWriter import AutoLogin
from writer.app.Browser import Firefox
from util.Secret import Secret

"""
Szenario: Ein Nutzer verwendet überall dasselbe Passwort, welches es rauszufinden gilt.
In Windows ist Autologin aktiviert und das Passwort lässt sich somit in der
Registry in Klartext finden. Hinweise?
Einschätzung: 3/5, 5/5 ohne Hinweise
"""

passwordSecret = str(Secret(password=True))
autologin = AutoLogin().enable('Eve', passwordSecret)
firefox = Firefox().googleSearch('enable autologin windows')
writer = AutoItScriptWriter()
writer.add(autologin).add(firefox).flush().writeSolutionInfo()
Secret().saveZip(writer.dirPath, 'secret.zip', passwordSecret)