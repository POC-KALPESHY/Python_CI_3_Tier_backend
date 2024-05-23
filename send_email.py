import smtplib
from email.mime.text import MIMEText

def send_email(status):
    sender_email = "onkarko@evolvingsols.com"
    receiver_email = "recipient@example.com"
    server_ip = "172.27.172.202"
    server_port = 25
    smtp_username = "onkarko@evolvingsols.com"
    smtp_password = "Cybage@87654321"

    message = MIMEText(f"The build job has {status}")
    message["Subject"] = "Build Status Notification"
    message["From"] = sender_email
    message["To"] = receiver_email

    try:
        server = smtplib.SMTP(server_ip, server_port)
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        server.quit()

if __name__ == "__main__":
    import sys
    status = sys.argv[1]
    send_email(status)
