import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
load_dotenv()
app_password=os.getenv("APP_PASSWORD")
sender=os.getenv("SENDER")
# Email details
def send_email(receiver_email: str, subject: str, content: str) -> str:
    """Send an email to the receiver with the given subject and content."""
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(content)

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, app_password)
        server.send_message(msg)

    return f"Email sent successfully to {receiver_email}!"