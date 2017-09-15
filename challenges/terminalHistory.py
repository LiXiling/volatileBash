# -*- coding: utf-8 -*-

from writer.Scripter import AutoItScriptWriter
from writer.app.Application import CMDApplication
from writer.app.SevenZip import SevenZip
from util.Secret import Secret

"""
Szenario: Ein Zipfile wurde mit 7z über eine cmd-Konsole erstellt und verschlüsselt.
Das Passwort lässt sich im Klartext in der cmd-history finden.
Einschätzung: 3/5
"""

passwordSecret = Secret('Password')
secret = Secret()
cmd = CMDApplication().add(SevenZip().createZip('secret.zip', str(passwordSecret)))
writer = AutoItScriptWriter()
writer.add(cmd).flush().writeSolutionInfo()
secret.saveZip(writer.dirPath , 'secret.zip', str(passwordSecret))

