from flask import Flask, render_template, request, redirect, flash , jsonify
from flask_mail import Mail, Message
import os

app = Flask(__name__, static_url_path='/static')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
app.secret_key = os.getenv('SECRET')

mail = Mail(app)

@app.route('/')
def index():
    # Project data
    projects = [
        {
            "id": 1,
            "title": "TOI19",
            "description": "I have competed in the Thailand Olympics of Informatics and achieved 24th out of 90",
            "image": "images/index/TOI19.jpg"
        },
        {
            "id": 2,
            "title": "NSC25 : Scambuster",
            "description": "I have contributed in making the application to filter spam messages and calls.",
            "image": "images/index/NSC_2.jpg"
        },
        {
            "id": 3,
            "title": "Super AI Engineer Season 4",
            "description": "I have participated and achieved bronze medal from Super AI Engineer Season 4",
            "image": "images/index/hero3.jpg"
        }
    ]
    return render_template('index.html' , projects = projects)

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        name = request.form['name']
        email = request.form['email']
        message_body = request.form['message']

        # Create the email message
        msg = Message(
            subject=f"New Contact Form Submission from {name}",
            sender=app.config['MAIL_DEFAULT_SENDER'],
            recipients=['sakukieng@gmail.com'],
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_body}"
        )

        mail.send(msg)
        flash('Email sent successfully!', 'success')
    except Exception as e:
        flash(f'Failed to send email. Error: {str(e)}', 'danger')
        
@app.route('/portfolio')
def portfolio() :
    return render_template('WIP.html')

@app.route('/popgital')
def popgital() :
    return render_template('WIP.html')

@app.route('/info')
def info() :
    education = [
        {
            "name": "Saint Gabriel's College",
            "degree": "Primary School",
            "year": "2011-2017",
            "logo": "images/profile/SG.png"  # Path relative to static folder
        },
        {
            "name": "Saint Gabriel's College",
            "degree": "High School",
            "year": "2017-2023",
            "logo": "images/profile/SG.png"
        },
        {
            "name": "KMUTT",
            "degree": "Undergraduate degree",
            "year": "2024-Now",
            "logo": "images/profile/KMUTT.png"
        }
    ]
    return render_template('About_me.html' , education=education)

if __name__ == '__main__':
    app.run(debug=True , threaded = True)