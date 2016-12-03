import os

import Writable
from FileCreator import FileCreator
from volatileApp.Application import Application


class ScriptWriter(FileCreator):
    _header = '#This script was generated by volatileBash\n' \
              'echo Do you want to run the Application Installer? [Y/N]\n' \
              'read input\n' \
              'if [[ $input =~ ^([yY][eE][sS]|[yY])$ ]]\n' \
              'then\n' \
              '\techo Installing...\n' \
              '\tbash ./installer.sh\n' \
              'else\n' \
              '\techo Skipping Installer\n' \
              'fi\n\n' \
              'true'

    def __init__(self, filePath):
        super(ScriptWriter, self).__init__(filePath)
        self.writables = []

    def add(self, writable):
        self.writables.append(writable)

        return self

    def andParalell(self, writable):
        self.writables.append(Writable.ParalellAnd())
        self.writables.append(writable)

        return self

    def getContent(self):
        content = self._header

        for writable in self.writables:
            content += ' & ' + str(writable)

        return content

    def _makeInstaller(self):
        installerPath = os.path.dirname(self.filePath) + '/installer.sh'

        self._createFile(installerPath)

        f = open(installerPath, 'a')
        for writable in self.writables:
            if isinstance(writable, Application):
                f.write(writable.install() + '\n')
        f.close()

        return self

    def _makeScript(self):
        self._createFile()

        f = open(self.filePath, 'a')
        f.write(self.getContent())
        f.close()

        return self

    def flush(self):
        self._makeScript()
        self._makeInstaller()
