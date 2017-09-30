#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""
##########################
# imports                #
##########################

import random
from writer.Scripter import AutoItScriptWriter, ShellScriptWriter
from util.Secret import Secret
from writer.app.ImageViewer import IrfanView
from writer.app.Network import Netcat, Wireshark

##########################
# setup writer           #
##########################

writer = AutoItScriptWriter()
shellScriptWriter = ShellScriptWriter(writer.extraDirPath)

##########################
# generate secrets       #
##########################

lowestPort = 42042
amount = 15
correctPort=random.randint(lowestPort, lowestPort+amount)
filename = "hint.png"
Secret("Watch out for port\n{}".format(correctPort), markAsFlag=False).saveImage(writer.dirPath, filename)

##########################
# setup applications     #
##########################

for i in range(amount):
    port = lowestPort+i
    secret = Secret()
    if port == correctPort:
        secret.saveImage(writer.extraDirPath, 'correctSecret.png')
    server = Netcat().listen(port)
    client = Netcat().send("The secret is {}".format(secret), host="$1", port=port)
    writer.add(server)
    shellScriptWriter.add(client)
wireshark = Wireshark().capture(port=lowestPort, lastPort=port)
imageviewer = IrfanView().openFile(filename)

##########################
# applications to writer #
##########################

writer.add(wireshark).add(imageviewer)

##########################
# generate script        #
##########################

shellScriptWriter.flush()
writer.flush()
writer.writeSolutionInfo()