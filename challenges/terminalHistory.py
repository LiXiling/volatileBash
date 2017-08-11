# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:46:04 2017

@author: Victor
"""

import os
import shutil

from volatileIO.AutoItScriptWriter import AutoItScriptWriter
from volatileAppWin.WinApplication import WinCMDApplication
from volatileAppWin.WinSevenZip import WinSevenZip
from volutil.Secret import Secret

outDir = "./output/"

if os.path.exists(outDir):
    shutil.rmtree(outDir)

"""
Szenario: Ein Zipfile wurde mit 7z über eine cmd-Konsole erstellt und verschlüsselt.
Das Passwort lässt sich im Klartext in der cmd-history finden.
Einschätzung: 3/5
"""


passwordSecret = Secret('Password')
secret = Secret()
cmd = WinCMDApplication().add(WinSevenZip().createZip('Secret.zip', str(passwordSecret)))
AutoItScriptWriter(outDir).add(cmd).flush()
secret.saveZip(outDir+'out.zip', str(passwordSecret))

