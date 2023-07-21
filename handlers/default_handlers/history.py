import json

from loader import bot
from telebot.types import Message
from main import db_read
from database.common.models import History


@bot.message_handler(commands=["history"])
def bot_history(message: Message):
    history_request = db_read(History, user_id=message.from_user.id)
    bot.reply_to(message, history_request)

