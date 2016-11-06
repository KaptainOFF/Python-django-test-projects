#!/usr/bin/env python3

import datetime

from collections import OrderedDict
from peewee import *

db = SqliteDatabase('diary.db')


class Entry(Model):
    # content
    content = TextField()
    # timestamp
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize():
    db.connect()
    db.create_table(Entry, safe=True)


def menu_loop():
    """Menu Loop"""
    choice = None

    while choice != 'q':
        print("Enter 'q' to exit")
        for key, value in menu.items():
            print("{}) {}".format(key, value.__doc__))

        choice = input("Action: ").lower().strip()

        if choice in menu:
            menu[choice]()


def add_entry():
    """Adds an entry to the diary"""


def view_entries():
    """Displays all the entries from the database"""


def remove_entry(entry):
    """Removes a specific entry from the database"""

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries)
])

if __name__ == '__main__':
    initialize()
    menu_loop()
