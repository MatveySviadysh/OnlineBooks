import aiohttp
from aiohttp import web
from handlers.email_handler import *

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