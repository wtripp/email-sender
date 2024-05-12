# Email Sender
This microservice takes as input a set of email details (sender, recipients, subject, body) and sends the email on behalf of a client. Use this microservice to enable sending emails directly from your application. Email Sender was built with Flask, a Python web application framework.

## Prerequisites
* You have Python 3.x installed.
* You have pip installed. See [installation - pip documentation](https://pip.pypa.io/en/stable/installation/).
* You have an email address that you want to use to send emails.

## Installation and Setup
1. Download `email-sender.py` from this repo.
2. Install the required dependencies.
```
pip install Flask
pip install flask-mail
```
3. Run the downloaded `email-sender.py` file. For example:
```
python3 email-sender.py
```
By default, the microservice runs on port 5000 of your localhost. You should see this output:

_\* Serving Flask app 'email-sender'_

_\* Debug mode: off_

_WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead._

_\* Running on http://127.0.0.1:5000_

_Press CTRL+C to quit_

## Request Data from Microservice 
To request data from the microservice, send a POST request to the `send-email` route of the host and port that the service is running on (default = http://localhost:5000/send-email). Send the following JSON fields in the post request:

#### Sender Parameters
* `mail_server` - Mail server of your email client. Example: `"smtp.gmail.com"`.
* `mail_port` - Port that your mail server uses. Example: `"587"' (commonly used port that gmail, Microsoft 365, and other mail servers use) 
* `mail_username` - Email address you want to use to send emails. Example: `"myfirstname.mylastname@gmail.com`
* `mail_password` - Password for your email address. If you have 2-factor authentication setup on your email, you might need to use an app password instead of your regular password. The instructions for setting up an app password vary by mail server. For example, to setup a mail client on Google:
    1.	Sign in to your [Google Account](https://myaccount.google.com/).
    2.	Search for `"app password"` and select the **App passwords** result.
    3.	Enter the name of your app and click **Create**.
    4.	Copy the app password to your clipboard and click **Done**.
    5.	Paste the app password into this field.

#### Email Parameters
* `recipients` - List of email addresses you want to send the email to. Example: `["recipient1@yahoo.com", "recipient2@gmail.com"]'
* `subject` - Subject line of email. Example: `"Example subject line"`
* `body` - Message body of email. If `html` is set to 'True', then the email accepts HTML tags. Example: `"Example message body"`.

#### Optional Parameters
* `html` - Format message body using email tag, specified as `true` or `false`. The default is `false` (send emails as plain text).
* `attachements` - List of files to attach to the email. Specify the full path to each attachment. If you omit this field, then the email includes no attachments. Example: `["file1.txt","img/file2.png"]`

### Sample Python Client
This sample client assumes that the email sender is already running.

1. Download the `test-client.py` and `.env` files from this repo.
2. Install the required dependencies.
```
    pip install dotenv
    pip install requests
```
3. In the `.env` file, set the `SERVER`, `PORT`, `USERNAME`, and `PASSWORD` environment variables. These correspond to the [Sender Parameters](#sender-parameters).
> **_SECURITY CONSIDERATIONS:_** DO NOT commit this file to any public repos. Store this file locally to keep your email credentials private.

4. In the `test-client.py` file, set the [Sender Parameters](#sender-parameters) and [Optional Parameters](#optional-parameters).

5. Run `test-client.py`. For example:
```
python3 test-client.py
```

### Sample curl Client
If you have `curl` installed, you can send emails by running a `curl` command like the following. Customize the fields below to suit your application.
```
curl -X POST -H "Content-Type: application/json" -d '{
"mail_server": "smtp.gmail.com",
"mail_port": "587",
"mail_username": "my_username@gmail.com",
"mail_password": "password123",
"recipients": ["recipient@gmail.com"],
"subject": "Example subject line",
"body": "Example message body of the email"
}' http://localhost:5000/send-email
```

## Receive Data from Microservice
When you send a request to the email sender microservice, it automatically returns a JSON response indicating whether the email was sent successfully or not.

If the message was sent successully, the microservice sends back this response:
```
{"message":"Email sent successfully.","success":true}
```
If this email failed to send, the microservice sends the error that triggered the failure. For example:
```
{'message': 'Missing required parameters: subject, body', 'success': False}
```
### UML Sequence Diagram
![UML sequence diagram of the Email Sender microservice](https://github.com/wtripp/email-sender/blob/master/a8-uml.png?raw=true)
