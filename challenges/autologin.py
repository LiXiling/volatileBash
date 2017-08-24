# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 13:57:45 2017

@author: Victor
"""
from volatileIO.Scripter import AutoItScriptWriter
from volatileIO.AuxWriter import AutoLogin
from volatileApp.Browser import Firefox
from volutil.Secret import Secret

"""
Szenario: Ein Nutzer verwendet überall dasselbe Passwort, welches es rauszufinden gilt.
In Windows ist Autologin aktiviert und das Passwort lässt sich somit in der
Registry in Klartext finden. Hinweise?
Einschätzung: 3/5, 5/5 ohne Hinweise
"""

passwordSecret = Secret('Password')
autologin = AutoLogin().enable('Eve', passwordSecret.obfuscate())
firefox = Firefox().googleSearch('enable autologin windows')
writer = AutoItScriptWriter()
writer.add(autologin).add(firefox).flush().writeSolutionInfo()
Secret().saveZip(writer.dirPath, 'out.zip', str(passwordSecret))