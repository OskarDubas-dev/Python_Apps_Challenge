import smtplib
import ssl
import os


def send_email(email, message):
    host = "smtp.gmail.com"
    port = 465
    password = os.getenv("PASSWORD_PORTFOLIO")
    username = os.getenv("USERNAME_PORTFOLIO")
    receiver = os.getenv("USERNAME_PORTFOLIO")
    context = ssl.create_default_context()

    _message = f"""\
Subject: Contact Us form (Portfolio Website)

{message}

From: {email}
"""

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, _message)
