from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os

app = Flask(__name__)
mail = Mail(app)

@app.route('/send-email', methods=['POST'])
def send_email():


    data = request.get_json()

#    if not all([mail_server, mail_port, mail_username, mail_password, recipients, subject, body]):
#       return jsonify({'error': 'Missing required parameters'}), 400

    try:
        app.config['MAIL_SERVER'] = data.get('mail_server')
        app.config['MAIL_PORT'] = data.get('mail_port')
        app.config['MAIL_USERNAME'] = data.get('mail_username')
        app.config['MAIL_PASSWORD'] = data.get('mail_password')
        app.config['MAIL_USE_TLS'] = True
        app.config['MAIL_USE_SSL'] = False
        mail = Mail(app)
        msg = Message(
            sender=data.get('mail_username'),
            subject=data.get('subject'),
            recipients=data.get('recipients')
        )

        msg.html = data.get('body')
        #msg.body = data.get('body')

        attachments = data.get('attachments')
        for attachment in attachments:
            with app.open_resource(attachment) as file:
                _, ext = os.path.splitext(attachment)
                msg.attach(attachment, f"application/{ext}", file.read())

        mail.send(msg)

        return "Message sent!"
    except Exception as e:
        return f"Message failed! Error: {e}"

if __name__ == '__main__':
    app.run(debug=True, port=5000)