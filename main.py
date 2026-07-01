 import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_ADDRESS, EMAIL_PASSWORD


def send_email(receiver_email, subject, body):

    # Create message object
    msg = MIMEMultipart()

    msg['From'] = EMAIL_ADDRESS
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add message body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)

        # Start encryption
        server.starttls()

        # Login
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # Send email
        server.send_message(msg)

        print("✅ Email sent successfully!")

    except Exception as e:
        print("❌ Error occurred:")
        print(e)

    finally:
        server.quit()


# User input
receiver = input("Enter recipient email: ")
subject = input("Enter subject: ")
message = input("Enter message: ")

# Send email
send_email(receiver, subject, message)