from dotenv import load_dotenv
import requests
import os

# Create email
load_dotenv()
data = {

    # Sender parameters (variables pulled from .env file)
    "mail_server": os.getenv("SERVER"),
    "mail_port": os.getenv("PORT"),
    "mail_username": os.getenv("USERNAME"),
    "mail_password": os.getenv("PASSWORD"),

    # Email parameters (update with email data; can be taken from CLI or GUI)
    "recipients": ["recipient1@example.com","recipient2@example.com"],
    "subject": 'Example subject line',
    "body": 'Example message body of the email',

    # Optional parameters (can be deleted if not used)
    "html": False,
    "attachments": ["attachment1.txt", "attachment2.txt"]
}

# Send email
url = 'http://localhost:5000/send-email'
response = requests.post(url, json=data)
print(response.json())