#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
##########################
# imports                #
##########################

from writer.FileCreator import FileWriter
from writer.Scripter import AutoItScriptWriter, ShellScriptWriter
from util.Secret import Secret
from writer.app.Network import Netcat, Wireshark

##########################
# setup writer           #
##########################


writer = AutoItScriptWriter()
shellScriptWriter = ShellScriptWriter(writer.extraDirPath)
secretFilename = "secret.txt"
fileWriter = FileWriter(writer.extraDirPath, secretFilename)

##########################
# generate secrets       #
##########################

secretString = str(Secret())

##########################
# setup applications     #
##########################

split = len(secretString) // 2
fileWriter.setFileContent("The secret is\n{}\n{}".format(secretString[:split], secretString[split:])).flush()
ncClient = Netcat().sendFileContents(secretFilename, host="$1")
ncServer = Netcat().listen()
wireshark = Wireshark().capture()

##########################
# applications to writer #
##########################

writer.add(ncServer).add(wireshark)
shellScriptWriter.add(ncClient)

##########################
# generate script        #
##########################

writer.flush()
writer.writeSolutionInfo()
shellScriptWriter.flush()