from handlers.default_handlers.text_message import ask_flight_schedule
from keyboards.inline.information import choice_inform
from loader import bot
from states.state import StateMessage
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP

from utils.API_commands import flight_schedule_information


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
                with bot.retrieve_data(call.message.chat.id, call.message.chat.id,) as data:
                    if call.data == "arrival":
                        data['direction'] = "arrival"
                    else:
                        data['direction'] = "departure"
                calendar, step = DetailedTelegramCalendar().build()
                bot.send_message(call.message.chat.id,
                                 f"Select {LSTEP[step]}",
                                 reply_markup=calendar)
                bot.set_state(call.message.chat.id, StateMessage.airport_schedule_fromLocal)
            elif call.data == "0_2":
                with bot.retrieve_data(call.message.chat.id, call.message.chat.id, ) as data:
                    data['timefrom'] = "T00:00"
                    data['timeto'] = "T02:00"
                ask_flight_schedule(call.message)
            elif call.data == "2_4":
                with bot.retrieve_data(call.message.chat.id, call.message.chat.id, ) as data:
                    data['timefrom'] = "T02:00"
                    data['timeto'] = "T04:00"
                ask_flight_schedule(call.message)
            elif call.data == "4_6":
                with bot.retrieve_data(call.message.chat.id, call.message.chat.id, ) as data:
                    data['timefrom'] = "T04:00"
                    data['timeto'] = "T06:00"
                ask_flight_schedule(call.message)
            elif call.data == "6_8":
                with bot.retrieve_data(call.message.chat.id, call.message.chat.id, ) as data:
                    data['timefrom'] = "T06:00"
                    data['timeto'] = "T08:00"
                ask_flight_schedule(call.message)
            elif call.data == "8_10":
                with bot.retrieve_data(call.message.chat.id, call.message.chat.id, ) as data:
                    data['timefrom'] = "T08:00"
                    data['timeto'] = "T10:00"
                ask_flight_schedule(call.message)
            elif call.data == "10_12":
                with bot.retrieve_data(call.message.chat.id, call.message.chat.id, ) as data:
                    data['timefrom'] = "T10:00"
                    data['timeto'] = "T12:00"
            elif call.data == "12_14":
                with bot.retrieve_data(call.message.chat.id, call.message.chat.id, ) as data:
                    data['timefrom'] = "T12:00"
                    data['timeto'] = "T14:00"
            elif call.data == "14_16":
                with bot.retrieve_data(call.message.chat.id, call.message.chat.id, ) as data:
                    data['timefrom'] = "T14:00"
                    data['timeto'] = "T16:00"
                ask_flight_schedule(call.message)
            elif call.data == "16_18":
                with bot.retrieve_data(call.message.chat.id, call.message.chat.id, ) as data:
                    data['timefrom'] = "T16:00"
                    data['timeto'] = "T18:00"
                ask_flight_schedule(call.message)
            elif call.data == "18_20":
                with bot.retrieve_data(call.message.chat.id, call.message.chat.id, ) as data:
                    data['timefrom'] = "T18:00"
                    data['timeto'] = "T20:00"
                ask_flight_schedule(call.message)
            elif call.data == "20_22":
                with bot.retrieve_data(call.message.chat.id, call.message.chat.id, ) as data:
                    data['timefrom'] = "T20:00"
                    data['timeto'] = "T22:00"
                ask_flight_schedule(call.message)
            elif call.data == "22_24":
                with bot.retrieve_data(call.message.chat.id, call.message.chat.id, ) as data:
                    data['timefrom'] = "T22:00"
                    data['timeto'] = "T24:00"
                ask_flight_schedule(call.message)
                            # bot.send_message(call.message.chat.id,
                #                  "Введите начало диапазона поиска (в формате:  ГГГГ-ММ-ДДTЧЧ:мм), например: 2023-04-04T20:00):")
                # bot.set_state(call.message.chat.id, StateMessage.airport_schedule_fromLocal)

    except Exception as e:
        print(repr(e))
