from FileCreator import FileCreator


class EMLWriter(FileCreator):
    def __init__(self, filePath):
        super(EMLWriter, self).__init__(filePath)
        self.sender = "sender@email.com"
        self.receiver = "receiver@email.com"
        self.content = "The secret is herbalTea"
        self.subject = "This is not a secret Mail"

    def getContent(self):
        return "MIME-Version: 1.0\n" \
                       "Received: by 10.80.181.115 with HTTP; Mon, 28 Nov 2016 08:30:51 -0800 (PST)\n" \
                       "Date: Mon, 28 Nov 2016 17:30:51 +0100\n" \
                       "Delivered-To: {}\n" \
                       "Subject: {}\n" \
                       "From: {}\n" \
                       "To: {}\n" \
                       "Content-Type: multipart/alternative; boundary=94eb2c1989cebdaec705425efeb2\n" \
                       "\n" \
                       "--94eb2c1989cebdaec705425efeb2\n" \
                       "Content-Type: text/plain; charset=UTF-8\n" \
                       "Content-Transfer-Encoding: quoted-printable)\n" \
                       "\n" \
                       "{}\n" \
                       "--94eb2c1989cebdaec705425efeb2".format(
            self.receiver,
            self.subject,
            self.sender,
            self.receiver,
            self.content
        )

    def flush(self):
        self._createFile()

        f = open(self.filePath, 'a')
        f.write(self.getContent())
        f.close()