from telebot.types import Message
from telebot import types
from loader import bot
from states.state import StateMessage


def inform_keyboards(message: Message):
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text="Да", callback_data="inform")
    markup.add(button_yes)
    bot.send_message(message.chat.id, f'Интересуетесь ли вы информацией об аэропортах, рейсах и длительности полета?', reply_markup=markup)


def choice_inform(call: types.CallbackQuery):
    markup = types.InlineKeyboardMarkup()
    button_airport = types.InlineKeyboardButton(text="Аэропорт", callback_data="airport")
    markup.add(button_airport)
    button_flight = types.InlineKeyboardButton(text="Рейс", callback_data="flight")
    markup.add(button_flight)
    button_flight_schedule = types.InlineKeyboardButton(text="Расписание рейсов", callback_data="flight_schedule")
    markup.add(button_flight_schedule)
    button_distance = types.InlineKeyboardButton(text="Дистанция и длительность полета", callback_data="distance_time")
    markup.add(button_distance)
    bot.send_message(call.message.chat.id,
                     f'Какую информацию вы бы хотели получить?',
                     reply_markup=markup)


def choice_departure_arrival(message):
    markup = types.InlineKeyboardMarkup()
    button_arrival = types.InlineKeyboardButton(text="Arrival", callback_data="arrival")
    markup.add(button_arrival)
    button_departure = types.InlineKeyboardButton(text="Departure", callback_data="departure")
    markup.add(button_departure)
    bot.send_message(message.chat.id,
                     'Arrival or departure?',
                     reply_markup=markup)

def choice_period(message):
    markup = types.InlineKeyboardMarkup()
    button_0_2 = types.InlineKeyboardButton(text="00:00 - 02:00", callback_data="0_2")
    markup.add(button_0_2)
    button_2_4 = types.InlineKeyboardButton(text="02:00 - 04:00", callback_data="2_4")
    markup.add(button_2_4)
    button_4_6 = types.InlineKeyboardButton(text="04:00 - 06:00", callback_data="4_6")
    markup.add(button_4_6)
    button_6_8 = types.InlineKeyboardButton(text="06:00 - 08:00", callback_data="6_8")
    markup.add(button_6_8)
    button_8_10 = types.InlineKeyboardButton(text="08:00 - 10:00", callback_data="8_10")
    markup.add(button_8_10)
    button_10_12 = types.InlineKeyboardButton(text="10:00 - 12:00", callback_data="10_12")
    markup.add(button_10_12)
    button_12_14= types.InlineKeyboardButton(text="12:00 - 14:00", callback_data="12_14")
    markup.add(button_12_14)
    button_14_16 = types.InlineKeyboardButton(text="14:00 - 16:00", callback_data="14_16")
    markup.add(button_14_16)
    button_16_18 = types.InlineKeyboardButton(text="16:00 - 18:00", callback_data="16_18")
    markup.add(button_16_18)
    button_18_20 = types.InlineKeyboardButton(text="18:00 - 20:00", callback_data="18_20")
    markup.add(button_18_20)
    button_20_22 = types.InlineKeyboardButton(text="20:00 - 22:00", callback_data="20_22")
    markup.add(button_20_22)
    button_22_24 = types.InlineKeyboardButton(text="22:00 - 24:00", callback_data="22_24")
    markup.add(button_22_24)
    bot.send_message(message.chat.id,
                     'Выберите период?',
                     reply_markup=markup)
