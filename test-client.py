from dotenv import load_dotenv
import requests
import os

# Create email
load_dotenv()
data = {

    # Required parameters
    "mail_server": os.getenv("SERVER"),
    "mail_port": os.getenv("PORT"),
    "mail_username": os.getenv("USERNAME"),
    "mail_password": os.getenv("PASSWORD"),
    "recipients": [os.getenv("USERNAME")],
    "subject": 'Example subject line',
    "body": '<h1>Example message body of the email</h1>',

    # Optional parameters
    "html": True,
    "attachments": ["attachment1.txt", "attachment2.txt"]
}

# Send email
url = 'http://localhost:5000/send-email'
response = requests.post(url, json=data)
print(response.json())