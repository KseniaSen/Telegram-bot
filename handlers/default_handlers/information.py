from telebot.types import Message
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP

from keyboards.inline.information import inform_keyboards
from loader import bot
from states.state import StateMessage


@bot.message_handler(commands=["information"])
def bot_hello_world(message: Message):
    inform_keyboards(message)


# @bot.callback_query_handler(func=DetailedTelegramCalendar.func())
# def cal(c):
#     result, key, step = DetailedTelegramCalendar().process(c.data)
#     if not result and key:
#         bot.edit_message_text(f"Select {LSTEP[step]}",
#                               c.message.chat.id,
#                               c.message.message_id, reply_markup=key)
#     elif result:
#         bot.set_state(c.message.chat.id, StateMessage.flight)
#         #print(c.message.chat.id, c.message.message_id)
#         bot.edit_message_text(f"You selected {result}",
#                               c.message.chat.id,
#                               c.message.message_id)
