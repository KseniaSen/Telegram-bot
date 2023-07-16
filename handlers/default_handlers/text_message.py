from telebot.types import Message

from keyboards.inline.information import inform_keyboards

from loader import bot
from states.state import StateMessage
from utils.API_commands import airoport_information

@bot.message_handler(state=StateMessage.airport)
def ask_airport(message: Message):
    if len(message.text) == 3 and message.text.isalpha():
        inform = airoport_information(message.text.upper())
        bot.send_message(message.chat.id, f"Информация об аэропорте: {inform}")
        bot.delete_state(message.from_user.id, message.chat.id)
    else:
        bot.send_message(message.chat.id, f"Введенный вами код аэропорта неправильный. Пожалуйста, попробуйте еще раз.")

@bot.message_handler(state=StateMessage.flight)
def ask_airport(message: Message):
    bot.send_message(message.chat.id, "Информация о рейсе:")
    bot.delete_state(message.from_user.id, message.chat.id)

@bot.message_handler(state=StateMessage.flight_schedule)
def ask_airport(message: Message):
    bot.send_message(message.chat.id, "Расписание рейсов:")
    bot.delete_state(message.from_user.id, message.chat.id)

@bot.message_handler(state=StateMessage.distance_time)
def ask_airport(message: Message):
    bot.send_message(message.chat.id, "Дистанция/время полета между аэропортами:")
    bot.delete_state(message.from_user.id, message.chat.id)

# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@bot.message_handler(state=None)
def bot_echo(message: Message):
    if ("привет" or "приветствую" or "здравствуйте" or "добрый день" or "доброе утро" or "добрый вечер") in message.text.lower():
        bot.send_message(message.chat.id, f'Привет, {message.from_user.full_name}!')
        inform_keyboards(message)
    else:
        bot.reply_to(
            message, "Эхо без состояния или фильтра.\n" f"Сообщение: {message.text}"
        )


