from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib 


sender_email = "test@test.com"
receiver_email = "test2@test.com"
sender_pass = ""


# Creates a multipart/* type message.
message = MIMEMultipart()
# set message headers
message["from"] = sender_email
message["to"] = receiver_email
message["subject"] = "Test Email from Python"

body = "This is a test email sent from Python!"
message.attach(MIMEText(body, "plain"))

try:
    smtp = smtplib.SMTP(host="smtp.gmail.com", port=587)
    # smtp.ehlo()
    smtp.starttls()
    smtp.login(sender_email, sender_pass)
    text = message.as_string()
    smtp.sendmail(sender_email, receiver_email, text)
    print("email was sent...")
except Exception as e:
    print(f"Error: {e}")
    
finally:
    smtp.quit()