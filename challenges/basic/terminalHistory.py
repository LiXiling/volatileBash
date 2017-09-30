# -*- coding: utf-8 -*-

"""
Szenario: Ein Zipfile wurde mit 7z ueber eine cmd-Konsole erstellt und verschluesselt.
Das Passwort laesst sich im Klartext in der cmd-history finden.
Einschaetzung: 3/5
"""

##########################
# imports                #
##########################

from writer.Scripter import AutoItScriptWriter
from writer.app.Application import CMDApplication, Remove
from writer.app.Zip import SevenZip
from util.Secret import Secret, PasswordSecret

##########################
# setup writer           #
##########################

writer = AutoItScriptWriter()

##########################
# generate secrets       #
##########################

passwordSecret = str(PasswordSecret())
filename = secret.png
secret = Secret()
secret.saveZip(writer.dirPath, 'secret.zip', passwordSecret)

##########################
# setup applications     #
#########################

cmd = CMDApplication().add(SevenZip().createZip('secret.zip', passwordSecret, filename))

##########################
# applications to writer #
##########################

writer.add(cmd).add(Remove(filename))

##########################
# generate script        #
##########################

writer.flush().writeSolutionInfo()

