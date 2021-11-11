# import os
import smtplib
from email.message import EmailMessage


def in_email():

    to = ["timothy@vandereyken.be"]

    msg_body = """ Enter tekst for body here."""

    email_id = 'code@vandereyken.be'
    email_pass = '_T1LuGaCoRo_75'

    for ev in to:
        msg = EmailMessage()
        msg['Subject'] = 'You receive this email because...'
        msg['From'] = email_id
        msg['To'] = ev
        msg.set_content(msg_body)

    # if I want to attach a file
    #     files = ['thisdoc.pdf']
    #     for file in files:
    #         with open(file, 'rb') as f:
    #             data = f.read()
    #             name = f.name
    #
    #     msg.add_attachment(data, maintype = 'application', subtype='octet-stream', filename=name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_id, email_pass)
        smtp.send_message(msg)
        smtp.quit()


def out_email():
    import email
    import imaplib

    EMAIL = 'mymail@mail.com'
    PASSWORD = 'password'
    SERVER = 'imap.gmail.com'

    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(EMAIL, PASSWORD)
    mail.select('inbox')
    status, data = mail.search(None, 'ALL')
    mail_ids = []
    for block in data:
        mail_ids += block.split()

    for i in mail_ids:
        status, data = mail.fetch(i, '(RFC822)')
        for response_part in data:
            if isinstance(response_part, tuple):
                message = email.message_from_bytes(response_part[1])
                mail_from = message['from']
                mail_subject = message['subject']
                if message.is_multipart():
                    mail_content = ''

                    for part in message.get_payload():
                        if part.get_content_type() == 'text/plain':
                            mail_content += part.get_payload()
                else:
                    mail_content = message.get_payload()
                print(f'From: {mail_from}')
                print(f'Subject: {mail_subject}')
                print(f'Content: {mail_content}')