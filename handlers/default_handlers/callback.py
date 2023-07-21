from keyboards.inline.information import choice_inform
from loader import bot
from states.state import StateMessage


@bot.callback_query_handler(state=None, func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == "inform":
                choice_inform(call)
            elif call.data == "airport":
                bot.set_state(call.message.chat.id, StateMessage.airport)
                bot.send_message(call.message.chat.id, "Введите код аэропорта (3-значный IATA-код аэропорта. Например: AMS, SFO, LAX и т. д.)):")
            elif call.data == "flight":
                bot.set_state(call.message.chat.id, StateMessage.flight_code)
                bot.send_message(call.message.chat.id, "Введите номер рейса:")
            elif call.data == "flight_schedule":
                bot.set_state(call.message.chat.id, StateMessage.airport_schedule_code)
                bot.send_message(call.message.chat.id, "Введите код аэропорта (3-значный IATA-код аэропорта. Например: AMS, SFO, LAX и т. д.)):")
            elif call.data == "distance_time":
                bot.set_state(call.message.chat.id, StateMessage.distance_time_from)
                bot.send_message(call.message.chat.id, "Введите код аэропорта отправления (3-значный IATA-код аэропорта. Например: AMS, SFO, LAX и т. д.)):")
            elif call.data == "arrival" or call.data == "departure":
                #with bot.retrieve_data(call.message.chat.id, call.message.from_user.id) as data:
                 #   data['direction'] = "arrival"
                bot.send_message(call.message.chat.id,
                                 "Введите начало диапазона поиска (в формате:  ГГГГ-ММ-ДДTЧЧ:мм), например: 2023-04-04T20:00):")
                bot.set_state(call.message.chat.id, StateMessage.airport_schedule_fromLocal)

    except Exception as e:
        print(repr(e))
