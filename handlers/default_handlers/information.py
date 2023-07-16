from telebot.types import Message

from keyboards.inline.information import inform_keyboards
from loader import bot


@bot.message_handler(commands=["information"])
def bot_hello_world(message: Message):
    inform_keyboards(message)
