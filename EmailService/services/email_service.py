import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import aiohttp


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


def issuccess(success, message):
    if success:
        print(f"Email отправлен успешно: {message}")
    else:
        print(f"Ошибка при отправке email: {message}")

async def fetch_subscribers():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8001/api/mailing_list/mailing_list/emails/') as response:
            if response.status != 200:
                raise Exception(f'Error fetching subscribers: {response.status}')
            return await response.json()

async def add_subscriber(email):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://127.0.0.1:8001/api/mailing_list/mailing_list/emails/', json={'email': email}) as response:
            if response.status not in (200, 201):
                raise Exception(f'Error adding subscriber: {response.status}')
