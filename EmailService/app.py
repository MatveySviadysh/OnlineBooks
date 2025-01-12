from aiohttp import web
import aiohttp_cors
from api.api_email import subscribe_to_newsletter_api
from handlers.email_handler import error_handler

app = web.Application(middlewares=[error_handler])

cors = aiohttp_cors.setup(app, defaults={
    "http://localhost:8080": aiohttp_cors.ResourceOptions(
        allow_credentials=True,
        expose_headers="*",
        allow_headers="*"
    )
})

app.router.add_post('/subscribe', subscribe_to_newsletter_api)

for route in list(app.router.routes()):
    cors.add(route)

if __name__ == "__main__": 
    web.run_app(app, port=8888)
