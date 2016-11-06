import datetime

from peewee import *

db = SqliteDatabase('diary.db')


class Entry(Model):
    # content
    content = TextField()
    # timestamp
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def menu_loop():
    """Menu Loop"""
    pass


def add_entry():
    """Adds an entry to the diary"""


def view_entries():
    """Displays all the entries from the database"""


def remove_entry(entry):
    """Removes a specific entry from the database"""
