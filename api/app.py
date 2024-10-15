from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__, static_url_path='/static')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465  # SSL Port
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
app.secret_key = 'GGi!al'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message_body = request.form['message']

    # Create the email message
    msg = Message(
        subject=f"New Contact Form Submission from {name}",
        sender=app.config['MAIL_DEFAULT_SENDER'],  # This ensures it's coming from your defined sender
        recipients=['sakukieng@gmail.com'],  # Change this to the email you want to receive contact form submissions
        body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_body}"
    )

    try:
        mail.send(msg)
        flash('Email sent successfully!', 'success')
        return redirect('/')
    except Exception as e:
        flash(f'Failed to send email. Error: {str(e)}', 'danger')
        return redirect('/')

@app.route('/portfolio')
def portfolio() :
    return render_template('WIP.html')

@app.route('/popgital')
def popgital() :
    return render_template('WIP.html')

@app.route('/info')
def info() :
    return render_template('About_me.html')

if __name__ == '__main__':
    app.run(debug=True , threaded = True)