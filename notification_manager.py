from os import environ
import smtplib
from twilio.rest import Client

MY_EMAIL = environ.get("MY_EMAIL")
MY_PASS = environ.get("MY_PASS")
account_sid = environ.get("ACCOUNT_SID")
auth_token = environ.get("AUTH_TOKEN")
MY_PNO = environ.get("MY_PNO")
MY_PHONE = environ.get("MY_PHONE")


class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)
    def send_message(self, message_text):
        message = self.client.messages.create(
            body=message_text,
            from_= MY_PNO,
            to= MY_PHONE
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASS)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject: Flight Low Prices!\n\n{message}."
                )
                print(f"Email sent.")
