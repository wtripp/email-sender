from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email():

    # Get data from client
    data = request.get_json()

    # Validate required parameters
    required_params = ['mail_server','mail_port','mail_username','mail_password',
                'subject','recipients','body']
    missing_params = [param for param in required_params if param not in data]
    if missing_params:
        return jsonify(
            {'success': False,
             'message': f'Missing required parameters: {", ".join(missing_params)}'})

    # Set required parameters
    server = data.get('mail_server')
    port = data.get('mail_port')
    username = data.get('mail_username')
    password = data.get('mail_password')
    subject = data.get('subject')
    recipients = data.get('recipients')
    body = data.get('body')

    # Set optional parameters
    attachments = data.get('attachments')
    html = data.get('html')

    try:

        # Configure mail sender
        app.config['MAIL_SERVER'] = server
        app.config['MAIL_PORT'] = port
        app.config['MAIL_USERNAME'] = username
        app.config['MAIL_PASSWORD'] = password
        app.config['MAIL_USE_TLS'] = True
        app.config['MAIL_USE_SSL'] = False
        mail = Mail(app)

        # Format message
        msg = Message(
            sender=username,
            subject=subject,
            recipients=recipients
        )
        if html:
            msg.html = body
        else:
            msg.body = body

        # Add attachments
        if attachments:
            for attachment in attachments:
                with app.open_resource(attachment) as file:
                    _, ext = os.path.splitext(attachment)
                    msg.attach(attachment, f"application/{ext}", file.read())

        # Send message
        mail.send(msg)
        return jsonify(
            {
             'success': True,
             'message': 'Email sent successfully.'}
            )

    except Exception as e:
        return jsonify(
            {
             'success': False,
             'message': f'Error: {e}'}
            )


if __name__ == '__main__':
    app.run(debug=False, port=5000)