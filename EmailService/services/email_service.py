import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

async def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        return True, f"Письмо успешно отправлено на {recipient_email}"
    except Exception as e:
        return False, f"Ошибка при отправке письма: {e}"

