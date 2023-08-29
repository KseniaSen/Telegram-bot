import json
from datetime import datetime
import requests

from config_data.config import RAPID_API_KEY, HOST_API
from loader import bot
from main import db_write
from database.common.models import History
from utils.parsing_json import parsing_json_airoport, parsing_json_airoport_schedule, parsing_json_flight, parsing_json_distance_time_information


def airoport_information(message):
    url = "https://aerodatabox.p.rapidapi.com/airports/iata/" + message.text.upper()

    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": HOST_API,
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_response = response.json()
        info = parsing_json_airoport(json_response)
        data = [{"code": response.status_code, "message": info, "created_at": datetime.now(),
                 "user_id": message.from_user.id}]
        db_write(History, data)

        return info
    else:
        data = [{"code": response.status_code, "message": response.reason, "user_id": message.from_user.id}]
        db_write(History, data)

        return 'Произошла ошибка при получении данных.'


def flight_information(message):
    with bot.retrieve_data(message.chat.id, message.chat.id) as data:
        url = "https://aerodatabox.p.rapidapi.com/flights/number/" + str(data['flight_code']) + "/" + str(data['flight_date'])

    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": HOST_API,
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_response = response.json()
        info = parsing_json_flight(json_response[0])
        data = [{"code": response.status_code, "message": info, "created_at": datetime.now(),
                 "user_id": message.from_user.id}]
        db_write(History, data)
        return info
    else:
        data = [{"code": response.status_code, "message": response.reason, "user_id": message.from_user.id}]
        db_write(History, data)
        if response.status_code == 204:
            return 'Информация о рейсе не найдена.'
        else:
            return 'Произошла ошибка при получении данных.'


def flight_schedule_information(message):
    with (bot.retrieve_data(message.chat.id, message.chat.id) as data):

        url = "https://aerodatabox.p.rapidapi.com/flights/airports/iata/" + data['airport_schedule_code'] + "/" \
              + str(data['flight_date']) + data['timefrom'] + "/" + str(data['flight_date'])+ data['timeto']
        # data['fromLocal_date'] + "/" + data['toLocal_date']
    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": HOST_API,
    }
    querystring = {"direction": data['direction']}

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        json_response = response.json()
        info = parsing_json_airoport_schedule(json_response, data['direction'])
        data = [{"code": response.status_code, "message": info, "created_at": datetime.now(),
                 "user_id": message.from_user.id}]
        db_write(History, data)
        return info
    else:
        data = [{"code": response.status_code, "message": response.reason, "user_id": message.from_user.id}]
        db_write(History, data)
        return 'Произошла ошибка при получении данных.'


def distance_time_information(message):
    with bot.retrieve_data(message.chat.id, message.from_user.id) as data:
        url = "https://aerodatabox.p.rapidapi.com/airports/iata/" + data['from_airport_code'] + "/distance-time/"\
              + data['to_airport_code']

    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": HOST_API,
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_response = response.json()
        info = parsing_json_distance_time_information(json_response)
        data = [{"code": response.status_code, "message": info, "created_at": datetime.now(),
                 "user_id": message.from_user.id}]
        db_write(History, data)
        return info
    else:
        data = [{"code": response.status_code, "message": response.reason, "user_id": message.from_user.id}]
        db_write(History, data)
        return 'Произошла ошибка при получении данных.'
