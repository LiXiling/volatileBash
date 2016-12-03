import datetime

from FileCreator import FileCreator

DEFAULT_DATE = datetime.datetime.now()
DEFAULT_SENDER = "Anna@email.com"
DEFAULT_RECEIVER = "Bob@email.com"
DEFAULT_SUBJECT = "This is not a secret Mail"
DEFAULT_CONTENT = "The secret is herbalTea"


class EMLWriter(FileCreator):
    def __init__(self, filePath,
                 date=DEFAULT_DATE,
                 sender=DEFAULT_SENDER,
                 receiver=DEFAULT_RECEIVER,
                 subject=DEFAULT_SUBJECT,
                 content=DEFAULT_CONTENT):
        super(EMLWriter, self).__init__(filePath)
        self.setDate(date)
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.content = content

    def setDate(self, date):
        self.date = date.strftime("%a, %d %b %Y %H:%M:%S +0000 (GMT)")
        return self

    def setSender(self, sender):
        self.sender = sender
        return self

    def setReceiver(self, receiver):
        self.receiver = receiver
        return self

    def setSubject(self, subject):
        self.subject = subject
        return self

    def setContent(self, content):
        self.content = content
        return self

    def getContent(self):
        return "MIME-Version: 1.0\n" \
               "Received: by 10.80.181.115 with HTTP; {0}\n" \
               "Date: Mon, {0}\n" \
               "Delivered-To: {1}\n" \
               "Subject: {2}\n" \
               "From: {3}\n" \
               "To: {1}\n" \
               "Content-Type: multipart/alternative; boundary=94eb2c1989cebdaec705425efeb2\n" \
               "\n" \
               "--94eb2c1989cebdaec705425efeb2\n" \
               "Content-Type: text/plain; charset=UTF-8\n" \
               "Content-Transfer-Encoding: quoted-printable)\n" \
               "\n" \
               "{4}\n" \
               "--94eb2c1989cebdaec705425efeb2".format(
            self.date,
            self.receiver,
            self.subject,
            self.sender,
            self.content
        )

    def flush(self):
        self._createFile()

        f = open(self.filePath, 'a')
        f.write(self.getContent())
        f.close()
