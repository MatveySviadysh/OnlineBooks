from services.email_service import send_email
from aiohttp import web
from config import smtp_user, smtp_password

async def send_email_api(request):
    try:
        data = await request.json()
        recipient_email = data.get('recipient_email')
        subject = "Поздравление"
        body = "Поздравляем вас с успешным завершением проекта!"

        if not recipient_email:
            return web.json_response({'success': False, 'message': 'Не указан адрес получателя'}, status=400)
        success, message = await send_email(smtp_user, smtp_password, recipient_email, subject, body)
        if success:
            return web.json_response({'success': True, 'message': message}, status=200)
        else:
            return web.json_response({'success': False, 'message': message}, status=500)
    except Exception as e:
        return web.json_response({'success': False, 'message': f'Ошибка обработки запроса: {e}'}, status=500)

