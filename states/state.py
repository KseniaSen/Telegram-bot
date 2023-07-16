from telebot.handler_backends import State, StatesGroup


class StateMessage(StatesGroup):
    start = State()
    inform = State()
    airport = State()
    flight = State()
    flight_schedule = State()
    distance_time = State()
