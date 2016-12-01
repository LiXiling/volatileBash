from volatileApp.Browser import Browser
from volatileApp.Application import Application
from volatileIO.ScriptWriter import ScriptWriter
from volatileIO.MailWriter import MailWriter

outDir = "./output/"

firefox = Browser().googleSearch("sha256")
gedit = Application("gedit").addArg("./script.sh")

script = (
    ScriptWriter(outDir + "script.sh")
        .add(firefox)
        .add(gedit)
        .flush()
)

email = (
    MailWriter(outDir + "test.eml")
        .flush()
)