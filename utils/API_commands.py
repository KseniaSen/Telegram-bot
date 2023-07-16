import json

import requests

from config_data.config import RAPID_API_KEY, HOST_API
from loader import bot


def airoport_information(iata):
    url = "https://aerodatabox.p.rapidapi.com/airports/iata/" + iata

    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": HOST_API,
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return json.dumps(response.json(), indent=4)
    else:
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
        return json.dumps(response.json(), indent=4)
    else:
        return 'Произошла ошибка при получении данных.'
