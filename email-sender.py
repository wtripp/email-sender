from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email():
    """Send an email message using sender and email data received from the client."""

    data = request.get_json()
    missing = has_required_params(data)
    if missing:
        return jsonify({'success':False, 'message':f'Missing required parameters: {missing}'})

    try:
        sender = create_sender(data)
        message = create_message(data)
        sender.send(message)
        return jsonify({'success':True, 'message':'Email sent successfully.'})
    except Exception as error:
        return jsonify({'success':False, 'message':f'Error: {error}'})


def has_required_params(data):
    """Validate that the data received from the client has all required parameters."""

    required_params = ['mail_server','mail_port','mail_username','mail_password',
                       'subject','recipients','body']
    missing_params = [param for param in required_params if param not in data]

    # If any parameters are missing, return them as a comma-separated list.
    if missing_params:
        return ", ".join(missing_params)


def create_sender(data):
    """Create the email sender using data received from the client."""

    app.config['MAIL_SERVER'] = data.get('mail_server')
    app.config['MAIL_PORT'] = data.get('mail_port')
    app.config['MAIL_USERNAME'] = data.get('mail_username')
    app.config['MAIL_PASSWORD'] = data.get('mail_password')
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False

    sender = Mail(app)
    return sender


def create_message(data):
    """Create the email message using data received from the client."""

    message = Message(sender=data.get('mail_username'),
                      subject=data.get('subject'),
                      recipients=data.get('recipients'))

    if data.get('html'):
        message.html = data.get('body')
    else:
        message.body = data.get('body')
    
    attachments = data.get('attachments')
    if attachments:
        message = add_attachments(attachments, message)

    return message


def add_attachments(attachments, message):
    """Add attachments to the message."""

    for attachment in attachments:
        with app.open_resource(attachment) as file:
            _, ext = os.path.splitext(attachment)
            message.attach(attachment, f"application/{ext}", file.read())
    return message


if __name__ == '__main__':
    app.run(debug=False, port=5000)