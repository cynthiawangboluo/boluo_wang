import smtplib
import time
import imaplib
import email


ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "username" + ORG_EMAIL
FROM_PWD    = "password"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993


def read_email_from_gmail():

        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()

        for num in data[0].split():
            typ, data = mail.fetch(num, '(RFC822)')
            raw_email = data[0][1]
            raw_email_string = raw_email.decode('utf-8')
            email_message = email.message_from_string(raw_email_string)
            print(email_message)

read_email_from_gmail()
