# -*- coding: utf-8 -*-
"""
Szenario: Ein Nutzer verwendet ueberall dasselbe Passwort, welches es rauszufinden gilt.
In Windows ist Autologin aktiviert und das Passwort laesst sich somit in der
Registry in Klartext finden (easy-mode) oder im lsadump (hard-mode, ungetestet).
Ein Hinweis ist die Google-Suche in Internet Explorer, diese laesst sich z.B. mit 
volatility iehistory nachvollziehen.
Einschaetzung: 3/5 easy, 5/5 hard
"""

##########################
# imports                #
##########################

from writer.Scripter import AutoItScriptWriter
from writer.AuxWriter import AutoLogin
from writer.app.Browser import InternetExplorer
from util.Secret import Secret, PasswordSecret

##########################
# setup writer           #
##########################

writer = AutoItScriptWriter()

##########################
# generate secrets       #
##########################

passwordSecret = str(PasswordSecret())
Secret().saveZip(writer.extraDirPath, 'secret.zip', passwordSecret)

##########################
# setup applications     #
##########################

autologin = AutoLogin().enable('Eve', passwordSecret, easy=True)
ie = InternetExplorer().googleSearch('enable autologin windows')

##########################
# applications to writer #
##########################

writer.add(autologin).add(ie)

##########################
# generate script        #
##########################

writer.flush().writeSolutionInfo()
