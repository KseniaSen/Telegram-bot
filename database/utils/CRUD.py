from typing import Dict, List, TypeVar

import peewee as pw

from database.common.models import ModelBase, db


T = TypeVar("T")


def _store_date(model: T, *data: List[Dict]) -> None:
    """Функция для добавления записи в базу данных"""
    with db.atomic():
        model.insert_many(*data).execute()


def _retrieve_all_data(model: T, *columns: ModelBase) -> pw.ModelSelect:
    """Функция для получения данных из базы данных"""
    with db.atomic():
        response = model.select(*columns)

    return response


class CRUDInteface:
    @staticmethod
    def create():
        return _store_date

    @staticmethod
    def retrieve():
        return _retrieve_all_data


if __name__ == "__main__":

    CRUDInteface()
