import FileMaker


class EMLWriter:
    def __init__(self, path):
        self.path = path
        self.sender = "sender@email.com"
        self.receiver = "receiver@email.com"
        self.content = "The secret is herbalTea"
        self.subject = "This is not a secret Mail"

    def flush(self):
        FileMaker.makeFile(self.path)

        f = open(self.path, 'a')
        f.write("MIME-Version: 1.0\n"
                "Received: by 10.80.181.115 with HTTP; Mon, 28 Nov 2016 08:30:51 -0800 (PST)\n"
                "Date: Mon, 28 Nov 2016 17:30:51 +0100\n"
                )
        f.write("Delivered-To: {}\n"
                .format(self.receiver))
        f.write("Subject: {}.\n"
                .format(self.subject))
        f.write("From: {}.\n"
                .format(self.sender))
        f.write("To: {}.\n"
                .format(self.receiver))
        f.write("Content-Type: multipart/alternative; boundary=94eb2c1989cebdaec705425efeb2\n"
                "\n"
                "--94eb2c1989cebdaec705425efeb2\n"
                "Content-Type: text/plain; charset=UTF-8\n"
                "Content-Transfer-Encoding: quoted-printable)\n"
                "\n"
                )
        f.write(self.content + "\n")
        f.write("--94eb2c1989cebdaec705425efeb2")