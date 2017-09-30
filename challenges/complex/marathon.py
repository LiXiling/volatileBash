#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##########################
# imports                #
##########################

from writer.app.ImageViewer import IrfanView
from writer.app.Application import CMDApplication, Remove
from writer.app.Zip import SevenZip
from writer.app.Browser import InternetExplorer
from writer.app.Editor import Notepad
from writer.AuxWriter import ClipboardWriter, RegistryWriter
from writer.Scripter import AutoItScriptWriter
from util.Secret import Secret, PasswordSecret
import random

##########################
# setup writer           #
##########################

writer = AutoItScriptWriter()

##########################
# generate secrets       #
##########################

rot1 = random.randint(4,20)
rot2 = random.randint(4,20)
rot3 = random.randint(4,20)
zipPasswort = PasswordSecret()
hint1 = Secret("Hint1: It's rotated it by {}!".format(rot1), markAsFlag=False).saveZip(writer.dirPath, "hint1.zip", zipPasswort)
hint2 = "Hint2: It's rotated it by {}!".format(rot2)
hint3 = "Hint3: It's rotated it by {}!".format(rot3)
pictureName = "hint5.png"
registryPath = "HKEY_CURRENT_USER\Software\MaliciousApp"
hint4 = Secret(registryPath, markAsFlag=False).rot(rot1+rot2+rot3).saveImage(writer.dirPath, pictureName)
flag = Secret("Th15~iS~th3~l@st~0n3!")

##########################
# setup applications     #
##########################

cmd = CMDApplication().add(SevenZip().createZip("C:\\Users\\Eve\\Desktop\\hint1.zip", zipPasswort, "hint1.png"))
clipboard = ClipboardWriter().put(hint2)
notepad = Notepad().setWindowTitle(hint3).setWindowPosition(0,0)
ie = InternetExplorer().googleSearch("how does rotation cipher work")
imageviewer = IrfanView().openFile(pictureName).setWindowDimensions(1280, 720)
registry = RegistryWriter().createRegistryEntry("Final", flag, registryPath)

##########################
# applications to writer #
##########################

writer.add(registry).add(clipboard).add(notepad).add(ie).add(cmd).add(imageviewer).add(Remove(pictureName))

##########################
# generate script        #
##########################

writer.flush().writeSolutionInfo()
