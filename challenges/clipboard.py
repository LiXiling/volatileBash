# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 17:01:45 2017

@author: Victor
"""
from volatileIO.AuxWriter import ClipboardWriter
from volatileIO.EMLWriter import EMLWriter
from volatileIO.Scripter import AutoItScriptWriter
from volatileApp.Editor import Notepad
from volutil.Secret import Secret

"""
Szenario: Es ist ein Textfile geöffnet, indem sich das Flag offensichtlich
befinden müsste, doch es wurde anscheinend entfernt. Das Secret befindet sich 
im Clipboard.
Einschätzung: 2/5
"""

filename = 'out.eml'
content = "Bob! Don't let anyone know that the secret passphrase is .\n" \
        "You can use it to log into our file server.\n"\
        "xoxo, Alice"
notepad = Notepad().openFile(filename)
clipboard = ClipboardWriter().put(Secret().obfuscate())
writer = AutoItScriptWriter()
writer.add(clipboard).add(notepad).flush().writeSolutionInfo()
EMLWriter(writer.dirPath, filename, content = content).flush()