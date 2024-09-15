Sending emails in Python can be done using the built-in `smtplib` library, which defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon. Here's a basic guide on how to send an email using Python:

### 1. **Set Up SMTP Server Connection:**

First, you need to connect to an SMTP server. For example, you can use Gmail's SMTP server for sending emails.

### 2. **Log in to Your Email Account:**

You'll need to authenticate with the SMTP server using your email and password.

### 3. **Create the Email:**

You'll need to specify the sender, recipient, subject, and body of the email.

### 4. **Send the Email:**

Once the email is set up, you can send it using the SMTP server connection.

Here’s a basic example:

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email details
sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@example.com"
password = "your_password"

# Create the email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Test Email from Python"

# Email body
body = "This is a test email sent from Python!"
msg.attach(MIMEText(body, 'plain'))

# SMTP server setup
try:
    # Connect to Gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection

    # Log in to your account
    server.login(sender_email, password)

    # Send the email
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)

    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    # Close the server connection
    server.quit()
```

### **Explanation:**

1. **Importing Required Libraries:**

   - `smtplib`: Used for sending emails.
   - `email.mime`: Used to construct the email content, including subject, body, and attachments.

2. **Email Details:**

   - `sender_email`: Your email address.
   - `receiver_email`: The recipient's email address.
   - `password`: Your email account password (or an app-specific password if using Gmail with 2FA).

3. **Creating the Email:**

   - `MIMEMultipart`: Allows you to create a message with multiple parts (e.g., text, HTML, attachments).
   - `MIMEText`: Used to attach the plain text body to the email.

4. **Connecting to SMTP Server:**

   - `smtplib.SMTP('smtp.gmail.com', 587)`: Connects to Gmail's SMTP server on port 587.
   - `starttls()`: Secures the connection with TLS encryption.
   - `login()`: Authenticates with your email credentials.

5. **Sending the Email:**

   - `sendmail()`: Sends the email using the server connection.

6. **Error Handling and Cleanup:**
   - The `try-except-finally` block is used to handle any potential errors and ensure the server connection is closed properly.

### **Important Notes:**

- If you're using Gmail, you might need to enable "Less secure app access" or use an App Password if you have 2-factor authentication enabled.
- Make sure not to hard-code your email and password in the script. Consider using environment variables or a configuration file for better security.

This should cover the basics of sending an email with Python.
