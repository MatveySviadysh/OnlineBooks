import aiohttp
from aiohttp import web
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from config import smtp_user, smtp_password
from services.email_service import issuccess, send_email, fetch_subscribers, add_subscriber


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


async def newsletter_handler(request):
    """curl -X POST http://127.0.0.1:8888/newsletter -H "Content-Type: application/json" -d '{"message": "Обновление сервиса на версию 1.2.1"}'"""
    try:
        data = await request.json()
        message = data.get('message')
        subject = "Рассылка новостей"
        subscribers = await fetch_subscribers()
        subscribed_emails = [item['email'] for item in subscribers]
        responses = []
        for recipient_email in subscribed_emails:
            success, response_message = await send_email(smtp_user, smtp_password, recipient_email, subject, message)
            responses.append((recipient_email, success, response_message))

        success_count = sum(1 for _, s, _ in responses if s)
        failure_count = len(responses) - success_count

        if failure_count == 0:
            return web.Response(text=f"Рассылка завершена успешно. Сообщение отправлено {success_count} адресатам.", status=200)
        else:
            return web.Response(text=f"Рассылка завершена с ошибками. Успешно отправлено {success_count}, не удалось отправить {failure_count}.", status=500)
    except Exception as e:
        return web.Response(text=f"Ошибка при обработке запроса: {e}", status=400)