from services.email_service import send_email
from aiohttp import web
from config import smtp_user, smtp_password
from services.email_service import issuccess

async def handle_email_send(request, subject, body):
    """Обработчик отправки email с общими параметрами."""
    try:
        data = await request.json()
        recipient_email = data.get('recipient_email')
        if not recipient_email:
            return web.json_response({'success': False, 'message': 'Не указан адрес получателя'}, status=400)
        success, message = await send_email(smtp_user, smtp_password, recipient_email, subject, body)
        if success is None or message is None:
            return web.json_response({'success': False, 'message': 'Неизвестная ошибка отправки письма'}, status=500)
        issuccess(success, message)
        if success:
            return web.json_response({'success': True, 'message': message}, status=200)
        else:
            return web.json_response({'success': False, 'message': message}, status=500)
    except Exception as e:
        return web.json_response({'success': False, 'message': f'Ошибка обработки запроса: {e}'}, status=500)

async def send_email_api(request):
    """API для отправки поздравительного email."""
    subject = "Поздравление"
    body = "Поздравляем вас с успешным завершением проекта!"
    return await handle_email_send(request, subject, body)
"""
curl -X POST http://127.0.0.1:8888/send_email \
-H "Content-Type: application/json" \
-d '{
  "recipient_email": "matvejsvadys5@gmail.com",
  "subject": "Тестовая тема",
  "body": "Привет! Это тестовое письмо, отправленное через API."
}'

"""
async def subscribe_to_newsletter_api(request):
    """API для подписки на рассылку."""
    subject = "Подтверждение подписки"
    body = "Поздравляем! Вы успешно подписались на нашу рассылку."
    return await handle_email_send(request, subject, body)
"""
curl -X POST http://localhost:8888/subscribe \
  -H "Content-Type: application/json" \
  -d '{"recipient_email": "matvejsvadys5@gmail.com"}'
"""