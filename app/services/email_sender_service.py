from email.message import EmailMessage
import email.message
from email.mime.multipart import MIMEMultipart
import smtplib

class EmailSenderService:
    SMTP_SERVER = "smtp.office365.com"
    SMTP_PORT = 587
    USERNAME = "coetzeex@outlook.com"
    PASSWORD = "X@nM$l27!6!@MICR"

    @classmethod
    def send_email(cls, to, subject, body):
     
        email_message = EmailMessage()
        email_message["From"] = cls.USERNAME
        email_message["Subject"] = subject
        email_message["To"] = to
        email_message.set_content(body)
    
        try:
            with smtplib.SMTP(cls.SMTP_SERVER, cls.SMTP_PORT) as smtp:
                smtp.starttls()
                smtp.login(cls.USERNAME, cls.PASSWORD)
                smtp.send_message(email_message)
        except Exception as ex:
            print(ex) 