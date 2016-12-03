import Writable
from FileCreator import FileCreator


class ScriptWriter(FileCreator):
    _header = '#This script was generated by volatileBash\n' \
              'true'

    def __init__(self, filePath):
        super(ScriptWriter, self).__init__(filePath)
        self.lines = []

    def add(self, writable):
        self.lines.append(writable)

        return self

    def andParalell(self, writable):
        self.lines.append(Writable.ParalellAnd())
        self.lines.append(writable)

        return self

    def getContent(self):
        content = self._header

        for writable in self.lines:
            content += ' & ' + str(writable)

        return content

    def flush(self):
        self._createFile()

        f = open(self.filePath, 'a')
        f.write(self.getContent())
        f.close()
