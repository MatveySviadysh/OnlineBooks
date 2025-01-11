from aiohttp import web
from api.api_email import send_email_api
from handlers.email_handler import error_handler

app = web.Application(middlewares=[error_handler])
app.router.add_post('/send_email', send_email_api)

if __name__ == "__main__": 
    web.run_app(app, port=8888)
