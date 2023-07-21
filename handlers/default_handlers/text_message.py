from telebot.types import Message

from keyboards.inline.information import inform_keyboards, choice_departure_arrival

from loader import bot
from states.state import StateMessage
from utils.API_commands import airoport_information, flight_information, distance_time_information, \
    flight_schedule_information
from utils.parsing_json import parsing_json_airoport


@bot.message_handler(state=StateMessage.airport)
def ask_airport(message: Message):
    if len(message.text) == 3 and message.text.isalpha():
        inform = airoport_information(message)
        bot.send_message(message.chat.id, inform)
        bot.delete_state(message.from_user.id, message.chat.id)
    else:
        bot.send_message(message.chat.id, f"Введенный вами код аэропорта неправильный. Пожалуйста, попробуйте еще раз.")

@bot.message_handler(state=StateMessage.flight_code)
def ask_flight_code(message: Message):
    with bot.retrieve_data(message.chat.id, message.from_user.id) as data:
        data['flight_code'] = message.text
    bot.send_message(message.chat.id, "Введите дату рейса (в формате: ГГГГ-ММ-ДД, например: 2023-07-01):")
    bot.set_state(message.chat.id, StateMessage.flight)


@bot.message_handler(state=StateMessage.flight)
def ask_flight(message: Message):
    with bot.retrieve_data(message.chat.id, message.from_user.id) as data:
        data['flight_date'] = message.text
    inform_flight = flight_information(message)
    bot.send_message(message.chat.id, f"Информация о рейсе: {inform_flight}")
    bot.delete_state(message.from_user.id, message.chat.id)

@bot.message_handler(state=StateMessage.airport_schedule_code)
def ask_airport_schedule_code(message: Message):
    if len(message.text) == 3 and message.text.isalpha():
        with bot.retrieve_data(message.chat.id, message.from_user.id) as data:
            data['airport_schedule_code'] = message.text
        choice_departure_arrival(message)
    else:
        bot.send_message(message.chat.id,
                         f"Введенный вами код аэропорта неправильный. Пожалуйста, попробуйте еще раз.")

@bot.message_handler(state=StateMessage.airport_schedule_fromLocal)
def ask_from_Local_date(message: Message):
    with bot.retrieve_data(message.chat.id, message.from_user.id) as data:
        data['fromLocal_date'] = message.text
    bot.send_message(message.chat.id, "Введите конец диапазона поиска (в формате:  ГГГГ-ММ-ДДTЧЧ:мм), например: 2023-04-04T20:00) Должен быть больше начала диапазона поиска, но не более чем на 12 часов:")
    bot.set_state(message.chat.id, StateMessage.airport_schedule)

@bot.message_handler(state=StateMessage.airport_schedule)
def ask_flight_schedule(message: Message):
    with bot.retrieve_data(message.chat.id, message.from_user.id) as data:
        data['toLocal_date'] = message.text
    inform_flight_schedule = flight_schedule_information(message)
    bot.send_message(message.chat.id, f"{inform_flight_schedule}")
    bot.delete_state(message.from_user.id, message.chat.id)

@bot.message_handler(state=StateMessage.distance_time_from)
def ask_airport_from(message: Message):
    if len(message.text) == 3 and message.text.isalpha():
        with bot.retrieve_data(message.chat.id, message.from_user.id) as data:
            data['from_airport_code'] = message.text
            bot.send_message(message.chat.id, "Введите код аэропорта назначения (3-значный IATA-код аэропорта. Например: AMS, SFO, LAX и т. д.)):")
            bot.set_state(message.chat.id, StateMessage.distance_time)
    else:
        bot.send_message(message.chat.id,
                         f"Введенный вами код аэропорта неправильный. Пожалуйста, попробуйте еще раз.")

@bot.message_handler(state=StateMessage.distance_time)
def ask_airport_to(message: Message):
    with bot.retrieve_data(message.chat.id, message.from_user.id) as data:
        data['to_airport_code'] = message.text
    inform_distance_time = distance_time_information(message)
    bot.send_message(message.chat.id, f"Дистанция/время полета между аэропортами: {inform_distance_time}")
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


