import logging
import requests
from telegram import Update
from telegram.ext import CallbackContext
from app.config import ALL_BOOKS_URL

logger = logging.getLogger(__name__)

def search_books(update: Update, context: CallbackContext) -> None:
    query = update.message.text.lower()

    try:
        response = requests.get(ALL_BOOKS_URL)
        response.raise_for_status()
        books = response.json()

        results = []
        for book in books:
            if query in book["title"].lower():
                results.append(
                    f"📖 <b>{book['title']}</b>\n"
                    f"👤 Автор: {book['author']}\n"
                    f"📚 Жанр: {book['genre']}\n"
                    f"📅 Дата публикации: {book['publication_date']}\n"
                    f"🌐 Язык: {book['language']}\n"
                    f"📄 Страниц: {book['page_count']}\n"
                    f"⭐ Рейтинг: {book['rating']}\n"
                    f"🔗 Ссылка: {book['file_url']}\n"
                )

        if results:
            update.message.reply_text("Результаты поиска:\n" + "\n".join(results), parse_mode="HTML")
        else:
            update.message.reply_text("Книги не найдены.")
    except requests.RequestException as e:
        logger.error(f"Ошибка API: {e}")
        update.message.reply_text("Ошибка при поиске. Попробуйте позже.")
