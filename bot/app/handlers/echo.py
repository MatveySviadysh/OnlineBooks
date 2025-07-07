from telegram import Update
from telegram.ext import CallbackContext

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Вы сказали: {update.message.text}')
