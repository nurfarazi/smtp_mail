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
    

def check_new_mail(username, password, imap_url):
    # establish a connection
    mail = imaplib.IMAP4_SSL(imap_url)
    # authenticate
    mail.login(username, password)
    # select the mailbox you want to check
    mail.select("inbox")
    # search for specific mail
    result, data = mail.uid('search', None, "ALL")
    # get the list of email IDs
    email_ids = data[0].split()
    # get the most recent email ID
    latest_email_id = email_ids[-1]
    # fetch the email body (RFC822) for the given ID
    result, email_data = mail.uid('fetch', latest_email_id, '(BODY[TEXT])')
    raw_email = email_data[0][1].decode("utf-8")
    email_message = email.message_from_string(raw_email)
    print(f"New email: {email_message.get_payload()}")

# Replace with your actual details
username = "username"
password = "password"
imap_url = "imap.example.com"

check_new_mail(username, password, imap_url)