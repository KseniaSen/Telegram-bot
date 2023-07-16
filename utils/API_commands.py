import json
from datetime import datetime
import requests

from config_data.config import RAPID_API_KEY, HOST_API
from loader import bot
from main import db_write
from database.common.models import History


def airoport_information(iata):
    url = "https://aerodatabox.p.rapidapi.com/airports/iata/" + iata

    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": HOST_API,
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_response = json.dumps(response.json(), indent=4)
        data = [{"code": response.status_code, "message": response.json(), "created_at": datetime.now()}]
        db_write(History, data)
        return json_response
    else:
        data = [{"code": response.status_code, "message": response.reason}]
        db_write(History, data)
        return 'Произошла ошибка при получении данных.'

def flight_information(message):

    with bot.retrieve_data(message.chat.id, message.from_user.id) as data:
        url = "https://aerodatabox.p.rapidapi.com/flights/number/" + data['flight_code'] + "/" + data['flight_date']

    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": HOST_API,
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = [{"code": response.status_code, "message": response.json(), "created_at": datetime.now()}]
        db_write(History, data)
        return json.dumps(response.json(), indent=4)
    else:
        data = [{"code": response.status_code, "message": response.reason}]
        db_write(History, data)
        return 'Произошла ошибка при получении данных.'
