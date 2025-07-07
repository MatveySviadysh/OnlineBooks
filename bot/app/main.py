import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from app.config import TOKEN
from app.handlers.base import start, handle_search_button
from app.handlers.search import search_books
from app.handlers.echo import echo

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

def main():
    if not TOKEN:
        raise ValueError("TOKEN не найден. Убедитесь, что .env содержит переменную.")

    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.regex(r'^Найти книгу$'), handle_search_button))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, search_books))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
