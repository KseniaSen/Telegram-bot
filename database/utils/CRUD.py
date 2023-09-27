from typing import Dict, List, TypeVar

import peewee as pw

from database.common.models import ModelBase, db


T = TypeVar("T")


def _store_date(model: T, data: List[Dict]) -> None:
    """Функция для добавления записи в базу данных"""
    with db.atomic():
        model.insert_many(data).execute()


def _retrieve_all_data(model: T, *columns: ModelBase, user_id) -> pw.ModelSelect:
    """Функция для получения данных из базы данных"""
    his = ''
    with db.atomic():
        response = list(model.select().where(model.user_id == user_id).order_by(model.created_at.desc()).limit(5))
        for string in reversed(response):
            his = his + str(string.created_at) + ': ' + string.message + '\n'
    return his


class CRUDInteface:
    @staticmethod
    def create():
        return _store_date

    @staticmethod
    def retrieve():
        return _retrieve_all_data


if __name__ == "__main__":

    CRUDInteface()
