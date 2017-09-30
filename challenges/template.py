#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##########################
# imports                #
##########################

from writer.Scripter import AutoItScriptWriter
from util.Secret import Secret
from writer.app.Browser import InternetExplorer

##########################
# setup writer           #
##########################

writer = AutoItScriptWriter()

##########################
# generate secrets       #
##########################

secret = Secret()

##########################
# setup applications     #
##########################

ie = InternetExplorer()
ie.googleSearch(str(secret))

##########################
# applications to writer #
##########################

writer.add(ie)

##########################
# generate script        #
##########################

writer.flush()
writer.writeSolutionInfo()
