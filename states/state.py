from telebot.handler_backends import State, StatesGroup


class StateMessage(StatesGroup):
    start = State()
    inform = State()
    airport = State()
    flight_code = State()
    flight = State()
    airport_schedule_code = State()
    airport_schedule_fromLocal = State()
    airport_schedule = State()
    distance_time = State()
    distance_time_from = State()
