import smtplib
import ssl
import os


def send_email(input_message):
    host = "smtp.gmail.com"
    port = 465

    username = "afridimohamed38@gmail.com"
    password = os.getenv("APP_PASSWORD")

    receiver = "afridimohamed38@gmail.com"

    to_send_message = input_message
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, to_send_message)


if __name__ == "__main__":
    message = "Hey there\nuser@user.com"
    send_email(message)
