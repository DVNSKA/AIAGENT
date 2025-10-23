import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
load_dotenv()

def send_email( receiver_email, subject, text_body, html_body=None):
    """
    Sends an email using Gmail SMTP.

    Args:
        receiver_email (str): Recipient's email address.
        subject (str): Email subject.
        text_body (str): Plain text version of the email.
        html_body (str, optional): HTML version of the email.
    
    Returns: email sending status.
    """

    # Create the email message
    message = MIMEMultipart("alternative")
    sender_email=os.getenv("USER_EMAIL")
    password=os.getenv("APPPASSWORD")
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach text and optional HTML
    message.attach(MIMEText(text_body, "plain"))
    if html_body:
        message.attach(MIMEText(html_body, "html"))

    try:
        # Connect to Gmail's SMTP server
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.send_message(message)
        print("✅ Email sent successfully!")
        return "Successfully sent email."
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return f"Failed to send email: {e}"
    

# send_email( 'pabbisettyabhiram@gmail.com', 'test', 'sample test')
    