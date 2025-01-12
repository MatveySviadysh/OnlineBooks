import aiohttp
from aiohttp import web
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from config import smtp_user, smtp_password
from services.email_service import issuccess, send_email



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


async def handle_email_send(request, subject, body):
    try:
        data = await request.json()
        recipient_email = data.get('recipient_email')
        if not recipient_email:
            return web.json_response({'success': False, 'message': 'Recipient address not specified'}, status=400)

        subscribers = await fetch_subscribers()
        subscribed_emails = {item['email'] for item in subscribers}

        if recipient_email in subscribed_emails:
            return web.json_response({'success': False, 'message': 'This email has already received the invitation'}, status=400)

        success, message = await send_email(smtp_user, smtp_password, recipient_email, subject, body)

        if success is None or message is None:
            return web.json_response({'success': False, 'message': 'Unknown error sending email'}, status=500)

        issuccess(success, message)

        if success:
            try:
                await add_subscriber(recipient_email)
            except Exception as e:
                print(f'Warning: {e}')
            return web.json_response({'success': True, 'message': message}, status=200)
        else:
            return web.json_response({'success': False, 'message': message}, status=500)

    except Exception as e:
        return web.json_response({'success': False, 'message': f'Error processing request: {e}'}, status=500)


async def subscribe_to_newsletter_api(request):
    """API для подписки на рассылку."""
    subject = "Подтверждение подписки"
    body = "Поздравляем! Вы успешно подписались на нашу рассылку."
    return await handle_email_send(request, subject, body)

