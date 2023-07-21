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
