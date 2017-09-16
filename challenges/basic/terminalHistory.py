# -*- coding: utf-8 -*-

from writer.Scripter import AutoItScriptWriter
from writer.app.Application import CMDApplication
from writer.app.SevenZip import SevenZip
from util.Secret import Secret

"""
Szenario: Ein Zipfile wurde mit 7z ueber eine cmd-Konsole erstellt und verschluesselt.
Das Passwort laesst sich im Klartext in der cmd-history finden.
Einschaetzung: 3/5
"""

passwordSecret = Secret('Password')
secret = Secret()
cmd = CMDApplication().add(SevenZip().createZip('secret.zip', str(passwordSecret)))
writer = AutoItScriptWriter()
writer.add(cmd).flush().writeSolutionInfo()
secret.saveZip(writer.extraDirPath(), 'secret.zip', str(passwordSecret))

