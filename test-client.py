from dotenv import load_dotenv
import requests
import os

load_dotenv()

# Define your mail server configuration
mail_server = os.getenv("SERVER")
mail_port = os.getenv("PORT")
mail_username = os.getenv("USERNAME")
mail_password = os.getenv("PASSWORD")

# Define the email – could also come from CLI prompts or UI parameters
recipients = ['will.tripp@gmail.com']
subject = 'Example subject line'
body = '<h1>Example message body of the email</h1>'
attachments = ["attachment1.txt", "attachment2.txt"]

# Send email
data = {
"mail_server":mail_server,
"mail_port":mail_port,
"mail_username":mail_username,
"mail_password":mail_password,
"recipients":recipients,
"subject":subject,
"body":body,
"attachments":attachments
}

url = 'http://localhost:5000/send-email'
response = requests.post(url, json=data)
print(response)