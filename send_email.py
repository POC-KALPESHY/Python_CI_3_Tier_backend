import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(status):
    sender = "username@outlook.com"
    recipient = ["onkarko@evolvingsols.com"]
    SUBJECT = "Build Status Notification"
    smtpserver = "smtp-mail.outlook.com"
    port = 587
    senderpassword = "password"

    if status == "success":
        TEXT = """
            <html style="font-family:Calibri">
            <body>
            <div>
                Dear User,<br/><br/>
                All the stages in the pipeline are successfully passed. Hence, the pipeline is successfully completed.
            </div>
            <br/>
            Note: This is a system generated mail. Please do not reply to this mail. In case of queries, please feel free to contact
            <a href="mailto:onkarko@evolvingsols.com">Support</a>.
            <div>
            <br/>Thank You.<br/>
            </div>
            <br/>
            </body>
            </html>
            """
    else:
        TEXT = f"The build job has {status}"
    email_message = MIMEMultipart('alternative')
    email_message['From'] = sender
    email_message['To'] = ",".join(recipient)
    email_message['Subject'] = SUBJECT
    message_body = MIMEText(TEXT, 'html')
    email_message.attach(message_body)

    SSL_context = ssl.create_default_context()
    SSL_context.check_hostname = False
    SSL_context.verify_mode = ssl.CERT_NONE

    try:
        with smtplib.SMTP(smtpserver, port) as server:
            server.starttls(context=SSL_context)
            server.login(sender, senderpassword)
            server.sendmail(sender, recipient, email_message.as_string())
        print("Email sent successfully")
    except Exception as e:
        err_msg = f'Error: unable to send email: {e}'
        print(err_msg)

if __name__ == "__main__":
    import sys
    status = "success"
    send_email(status)
