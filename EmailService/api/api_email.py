from services.email_service import send_email
from aiohttp import web
from config import smtp_user, smtp_password
from services.email_service import issuccess

sent_emails = set()

async def handle_email_send(request, subject, body):
    """Обработчик отправки email с общими параметрами."""
    try:
        data = await request.json()
        recipient_email = data.get('recipient_email')
        
        if not recipient_email:
            return web.json_response({'success': False, 'message': 'Recipient address not specified'}, status=400)

        # Check if the email has already been sent
        if recipient_email in sent_emails:
            return web.json_response({'success': False, 'message': 'This email has already received the invitation'}, status=400)

        # Send the email
        success, message = await send_email(smtp_user, smtp_password, recipient_email, subject, body)

        if success is None or message is None:
            return web.json_response({'success': False, 'message': 'Unknown error sending email'}, status=500)
        
        issuccess(success, message)

        if success:
            # Add the email to the sent emails set
            sent_emails.add(recipient_email)
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

async def send_email_api(request):
    """API для отправки поздравительного email."""
    subject = "Поздравление"
    body = "Поздравляем вас с успешным завершением проекта!"
    return await handle_email_send(request, subject, body)
