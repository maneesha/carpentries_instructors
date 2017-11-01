import mimetypes
import smtplib
import getpass
import email
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import local_settings

# Use Mailgun credentials-
smtp_user = local_settings.smtp_user
smtp_passwd = local_settings.smtp_passwd

server = smtplib.SMTP('smtp.mailgun.org:587')
server.starttls()
server.login(smtp_user, smtp_passwd)

def send_email(email_to,email_subject,email_body,email_from="the Carpentries Team <team@carpentries.org>"):
    """
    Using a pre-rendered body, email
    """
    msg = MIMEMultipart('alternative')
    msg['Subject'] = email_subject
    msg['From'] = email_from
    msg['To'] = email_to
    msg.attach(MIMEText(email_body, 'html'))
    to_address = email_to
    from_address = email_from
    server.sendmail(from_address, to_address, msg.as_string())
