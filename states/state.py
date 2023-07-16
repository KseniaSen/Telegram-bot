from telebot.handler_backends import State, StatesGroup


class StateMessage(StatesGroup):
    start = State()
    inform = State()
    airport = State()
    flight_code = State()
    flight = State()
    flight_schedule_code = State()
    flight_schedule = State()
    distance_time = State()
