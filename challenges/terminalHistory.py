# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:46:04 2017

@author: Victor
"""
from volatileIO.Scripter import AutoItScriptWriter
from volatileApp.Application import CMDApplication
from volatileApp.SevenZip import SevenZip
from volutil.Secret import Secret

"""
Szenario: Ein Zipfile wurde mit 7z über eine cmd-Konsole erstellt und verschlüsselt.
Das Passwort lässt sich im Klartext in der cmd-history finden.
Einschätzung: 3/5
"""

passwordSecret = Secret('Password')
secret = Secret()
cmd = CMDApplication().add(SevenZip().createZip('Secret.zip', str(passwordSecret)))
writer = AutoItScriptWriter()
writer.add(cmd).flush().writeSolutionInfo()
secret.saveZip(writer.dirPath , 'out.zip', str(passwordSecret))

