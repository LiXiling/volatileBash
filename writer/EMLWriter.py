# -*- coding: utf-8 -*-

import datetime

from writer.FileCreator import FileCreator

# Static Constants for Default values
DEFAULT_DATE = datetime.datetime.now()
DEFAULT_SENDER = "Alice@email.com"
DEFAULT_RECEIVER = "Eve@email.com"
DEFAULT_SUBJECT = "This is not a secret Mail"
DEFAULT_CONTENT = "The secret is herbalTea"


class EMLWriter(FileCreator):
    '''
    Class used for creating EML email files.
    Implements the FileCreator
    '''

    def __init__(self,
                 dirPath,
                 fileName,
                 date=DEFAULT_DATE,
                 sender=DEFAULT_SENDER,
                 receiver=DEFAULT_RECEIVER,
                 subject=DEFAULT_SUBJECT,
                 content=DEFAULT_CONTENT):
        '''
        creates a new EMLWriter
        :param filePath: the path to the output file
        :param date: date on which the email is received
        :param sender: sender of the email
        :param receiver: receiver of the email
        :param subject: subject of the email
        :param content: content of the email
        '''
        super(EMLWriter, self).__init__(dirPath)
        self.FILENAME = fileName
        self.setDate(date)
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.content = content

    def setDate(self, date):
        '''
        parses a date and sets its value for the email
        :param date: a date object
        :return: the EMLWriter object for method chaining
        '''
        self.date = date.strftime("%a, %d %b %Y %H:%M:%S +0000 (GMT)")
        return self

    def setSender(self, sender):
        '''
        setter for the sender
        :param sender: the sender of the email
        :return: the EMLWriter object for method chaining
        '''
        self.sender = sender
        return self

    def setReceiver(self, receiver):
        '''
        setter for the receiver
        :param receiver: the receiver of the email
        :return: the EMLWriter object for method chaining
        '''
        self.receiver = receiver
        return self

    def setSubject(self, subject):
        '''
        setter for the subject
        :param subject: the subject of the email
        :return: the EMLWriter object for method chaining
        '''
        self.subject = subject
        return self

    def setContent(self, content):
        '''
        settter for the content
        :param content: the content of the email
        :return: the EMLWriter object for method chaining
        '''
        self.content = content
        return self

    def getFileContent(self):
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
