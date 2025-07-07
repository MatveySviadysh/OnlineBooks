from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext

def create_main_menu():
    keyboard = [[KeyboardButton("Найти книгу")]]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Доступные команды:\n"
        "1. Найти книгу - поиск книг по названию.\n"
        "2. /start - показать это сообщение.",
        reply_markup=create_main_menu()
    )

def handle_search_button(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Введите название книги для поиска:")
