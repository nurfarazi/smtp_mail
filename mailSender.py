import smtplib
import imaplib
import email
from email.header import decode_header

sender = "your_email@farazi.com"
receiver = "target-incl-tenant-2@appdev-mt.devensoft.com"
subject = "Email Subject"
body = "This is the email body."

message = f"From: {sender}\nTo: {receiver}\nSubject: {subject}\n\n{body}"

try:
    with smtplib.SMTP("localhost", 25) as server: 
        server.sendmail(sender, receiver, message)
    print("Email sent successfully!")
except smtplib.SMTPException as e:
    print(f"Failed to send email: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")