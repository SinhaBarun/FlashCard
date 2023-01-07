from email import encoders
from email.mime.base import MIMEBase
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Template


SMTP_SERVER_HOST = "localhost"
SMTP_SERVER_PORT = 1025
SENDER_ADDRESS = "abc@mail.com"
SENDER_PASSWORD = ""


def send_mail(to_add, subject, message, content="text", attachement_file=None):
    msg = MIMEMultipart()
    msg["From"] = SENDER_ADDRESS
    msg["To"] = to_add
    msg["Subject"] = subject

    if content == "html":
        msg.attach(MIMEText(message, "html"))
    else :
        msg.attach(MIMEText(message, "plain"))

    if attachement_file :
        with open(attachement_file, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition", f"attachment: filename = {attachement_file}"
        )

    msg.attach(part)

    s = smtplib.SMTP(host=SMTP_SERVER_HOST, port=SMTP_SERVER_PORT)
    s.login(SENDER_ADDRESS,SENDER_PASSWORD)
    s.send_message(msg)
    s.quit()

    return True

def format_message(template_file, data={}):
    with open(template_file) as file_x:
        template = Template(file_x.read())
        return template.render(data=data)

def send_welcome_message(data):
    message = format_message(template_file="mai.html", data=data)
    send_mail(data['email'],subject="html", message=message, content="html", attachement_file="ac.pdf")

