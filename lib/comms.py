# file comms.py
# This file stores information regarding the mailgun emailing 
# functions for MakersBnB
import requests
import os


# MakersBnB Mailgun API key and domain
MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')

MAILGUN_DOMAIN = os.environ.get('MAILGUN_DOMAIN')


class EmailManager():

    def __init__(self):
        pass

    def send_email(self, to, subject, text):
        return requests.post(
            f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
            auth=("api", MAILGUN_API_KEY),
            data={"from": "MakersBnB <series4000kryten@gmail.com>",
                    "to": to,
                    "subject": subject,
                    "text": text})

# if __name__ == "__main__":
#     to = "series4000kryten@gmail.com"
#     subject = "Test Email"
#     text = "This is a test email sent from Mailgun."
#     response = send_email(to, subject, text)
#     print(response.text)