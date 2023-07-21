from datetime import datetime

import peewee as pw

db = pw.SqliteDatabase('Logging.db')


class ModelBase(pw.Model):
    """Класс ModelBase"""
    created_at = pw.DateTimeField(default=datetime.now())

    class Meta:
        database = db


class History(ModelBase):
    """Класс History Родитель: ModelBase"""
    code = pw.TextField()
    message = pw.TextField()
    user_id = pw.TextField()
    #created_at = pw.DateTimeField(default=datetime.now())