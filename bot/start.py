import os
import logging
import requests
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# URL вашего API
All_BOOKS = "http://localhost:8001/api/books/books/all"

# Создаем клавиатуру с кнопкой "Найти книгу"
def create_main_menu():
    keyboard = [
        [KeyboardButton("Найти книгу")],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Команда /start
def start(update: Update, context: CallbackContext) -> None:
    # Отправляем список возможностей бота
    update.message.reply_text(
        "Доступные команды:\n"
        "1. Найти книгу - поиск книг по названию.\n"
        "2. /start - показать это сообщение.\n"
        "Используйте меню внизу для удобства.",
        reply_markup=create_main_menu()
    )

# Обработка нажатия на кнопку "Найти книгу"
def handle_search_button(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Введите название книги для поиска:")

# Поиск книг
def search_books(update: Update, context: CallbackContext) -> None:
    query = update.message.text.lower()  # Получаем текст сообщения как поисковый запрос

    try:
        # Отправляем GET-запрос к API для получения списка книг
        response = requests.get(All_BOOKS)
        response.raise_for_status()  # Проверяем, что запрос успешен
        books = response.json()  # Получаем JSON-ответ

        # Ищем книги по названию
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
            update.message.reply_text("Книги по вашему запросу не найдены.")

    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при запросе к API: {e}")
        update.message.reply_text("Произошла ошибка при поиске книг. Попробуйте позже.")

# Обработка текстовых сообщений
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Вы сказали: {update.message.text}')

def main():
    # Получаем токен из переменных окружения
    token = os.getenv('TOKEN')
    if not token:
        raise ValueError("Не задан токен бота. Убедитесь, что переменная TOKEN установлена в файле .env")

    # Инициализируем updater с токеном
    updater = Updater(token)

    dp = updater.dispatcher

    # Регистрируем обработчики команд
    dp.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик нажатия на кнопку "Найти книгу"
    dp.add_handler(MessageHandler(Filters.regex(r'^Найти книгу$'), handle_search_button))

    # Регистрируем обработчик текстовых сообщений для поиска книг
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, search_books))

    # Регистрируем обработчик текстовых сообщений (эхо)
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()