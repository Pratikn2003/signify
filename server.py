from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

# Email Configuration
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')

def send_email(to_email, subject, html_content):
    """Send email using SMTP"""
    try:
        # Create message
        msg = MIMEMultipart('alternative')
        msg['From'] = EMAIL_USER
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Attach HTML content
        html_part = MIMEText(html_content, 'html')
        msg.attach(html_part)
        
        # Connect to SMTP server and send
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

@app.route('/', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'success',
        'message': 'Signify Backend is running'
    })

@app.route('/api/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    try:
        # Get form data
        data = request.get_json()
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()
        
        # Validation
        if not name or not email or not message:
            return jsonify({
                'status': 'error',
                'message': 'Please fill all fields'
            }), 400
        
        # Email to Support Team
        support_html = f"""
        <div style="font-family: Arial, sans-serif; padding: 20px;">
            <h2 style="color: #333;">New Contact Form Message</h2>
            <hr>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Message:</strong></p>
            <p style="background: #f5f5f5; padding: 15px; border-radius: 5px;">{message}</p>
            <hr>
            <p style="color: #999; font-size: 12px;">Sent from Signify Contact Form</p>
        </div>
        """
        
        # Email to User (Auto-reply)
        user_html = f"""
        <div style="font-family: Arial, sans-serif; padding: 20px;">
            <h2 style="color: #4CAF50;">Thank You, {name}!</h2>
            <p>We have received your message and will get back to you as soon as possible.</p>
            <hr>
            <p><strong>Your message:</strong></p>
            <p style="background: #f5f5f5; padding: 15px; border-radius: 5px;">{message}</p>
            <hr>
            <p>Best regards,<br><strong>Signify Team</strong></p>
            <p style="color: #999;">Secure. Verify. Protect.</p>
        </div>
        """
        
        # Send email to support team
        support_sent = send_email(
            RECEIVER_EMAIL,
            f'New Contact Form Message from {name}',
            support_html
        )
        
        # Send auto-reply to user
        user_sent = send_email(
            email,
            'Thank you for contacting Signify',
            user_html
        )
        
        if support_sent and user_sent:
            return jsonify({
                'status': 'success',
                'message': 'Message sent successfully!'
            }), 200
        else:
            return jsonify({
                'status': 'error',
                'message': 'Failed to send email. Please check email configuration.'
            }), 500
            
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({
            'status': 'error',
            'message': 'Server error occurred'
        }), 500

if __name__ == '__main__':
    print("\n🚀 Signify Backend Server starting...")
    print(f"📧 Email: {EMAIL_USER}")
    print(f"📬 Receiver: {RECEIVER_EMAIL}")
    print("✅ Server running on http://localhost:5000\n")
    app.run(debug=True, host='0.0.0.0', port=5000)