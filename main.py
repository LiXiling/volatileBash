from volatileApp.Browser import Browser
from volatileApp.Application import Application
from volatileIO.ScriptWriter import ScriptWriter

writer = ScriptWriter("./script.sh")
firefox = Browser().googleSearch("sha256")
gedit = Application("gedit").addArg("./script.sh")

script = (
    writer
        .add(firefox)
        .add(gedit)
        .flush()
)