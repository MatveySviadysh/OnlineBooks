import aiohttp
from aiohttp import web
from handlers.email_handler import *
import os 

async def subscribe_to_newsletter_api(request):
    """API для подписки на рассылку."""
    subject = "Подтверждение подписки"
    body = "Поздравляем! Вы успешно подписались на нашу рассылку."
    return await handle_email_send(request, subject, body)



async def newsletter(request):
    """API для рассылки новостей."""
    subject = "Оповещение об новостях"
    body = "У нас  вышло обновление"
    await handle_email_send_news(request,subject, body)


async def send_user_email(request):
    print()
    """API для отправки письма от пользователя"""
    data = await request.json()

    message_body = data.get('message_body')

    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    SMTP_USER = os.getenv('SMTP_USER')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')

    msg = MIMEText(message_body)
    msg['Subject'] = 'Новое сообщение от пользователя'
    msg['From'] = SMTP_USER
    msg['To'] = SMTP_USER
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
        return web.json_response({'success': True})
    except smtplib.SMTPAuthenticationError:
        return web.json_response(
            {'success': False, 'message': 'Ошибка аутентификации. Проверьте логин и пароль.'},
            status=401
        )
    except Exception as e:
        return web.json_response({'success': False, 'message': str(e)}, status=500)
