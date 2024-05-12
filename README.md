# Email Sender Microservice
The Email Sender microservice takes as input a set of email details (sender, recipients, subject, body) and sends the email on behalf of a client. Use this microservice to enable sending emails directly from your application. Email Sender was built with Flask, a Python web application framework.

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#installation-and-setup">Installation and Setup</a></li>
    <li><a href="#request-data-from-microservice">Request Data from Microservice</a></li>
    <li><a href="#receive-data-from-microservice">Receive Data from Microservice</a></li>
    <li><a href="#uml-sequence-diagram">UML Sequence Diagram</a></li>
  </ol>
</details>

## Prerequisites
* You have Python 3.x installed.
* You have [pip](https://pip.pypa.io/en/stable/installation/) installed.

## Installation and Setup
1. Download `email-sender.py` from this repo.
2. Install the required dependencies for the microservice.
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
To request data from the microservice, send a POST request to `http://localhost:5000/send-email` that contains the following parameters in JSON format:

#### Sender Parameters
* `mail_server` - Hostname of your outgoing email server. Example: `"smtp.gmail.com"`.
* `mail_port` - Port that your email server uses. Example: `"587"` (port that Gmail and other SMTP email servers use) 
* `mail_username` - Email address you want to use to send emails. Example: `"myfirstname.mylastname@gmail.com"`
* `mail_password` - Email password. If your email account uses 2-factor authentication, you might need to use an app password instead of your regular password. The instructions for setting up an app password vary by email server. For example, to create an app password for Gmail:
    1.	Sign in to your [Google Account](https://myaccount.google.com/).
    2.	Search for `"app password"` and select the **App passwords** result.
    3.	Enter the name of your app and click **Create**.
    4.	Copy the app password to your clipboard and click **Done**.
    5.	Paste the app password into the `mail_password` parameter.

#### Email Parameters
* `recipients` - List of email addresses you want to send the email to. Example: `["recipient1@yahoo.com", "recipient2@gmail.com"]`
* `subject` - Subject line of email. Example: `"Example subject line"`
* `body` - Message body of email. If `html` is set to `true`, then you can use HTML tags in the message body. Example: `"Example message body"`

#### Optional Parameters
* `html` - Format the message body using HTML tagging, specified as `true` or `false`. The default is `false` (send emails as plain text).
* `attachements` - List of files to attach to the email. Specify the full path to each file. If you omit this parameter, then the email includes no attachments. Example: `["file1.txt","img/file2.png"]`

### Sample Python Client
Use this sample client to understand how to integrate the email sender microservice into a Python application. This sample client assumes that the email sender microservice is already running.

1. Download `test-client.py` from this repo.
2. Install the required dependencies for the client.
```
    pip install dotenv
    pip install requests
```
3. In the same folder as `test-client.py`, create a `.env` file with the structure below. Update the `SERVER`, `PORT`, `USERNAME`, and `PASSWORD` environment variables. These variables correspond to the [Sender Parameters](#sender-parameters).
> **_SECURITY CONSIDERATIONS:_** DO NOT commit this file to any public repos. Store this file locally to keep your email credentials private.
```
SERVER='<mail server, such as smtp.gmail.com>'
PORT='<mail port, such as 587>'
USERNAME='<email username>'
PASSWORD='<email password or app password>'
```

4. In `test-client.py`, set the [Sender Parameters](#sender-parameters) and [Optional Parameters](#optional-parameters).

5. Run `test-client.py`. For example:
```
python3 test-client.py
```

### Sample curl Client
If you have `curl` installed, you can send emails by running a `curl` command similar to the following. Customize the parameters for your application.
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
