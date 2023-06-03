from textwrap import dedent
from random import choice
import sqlite3
import os


def get_random_film():
    with sqlite3.connect('films.db') as connection:
        cur = connection.cursor()
        cur.execute('SELECT title FROM films ORDER BY RANDOM() LIMIT 1;')
        film = cur.fetchone()[0]
    return f'Your film - {film}'


if __name__ == '__main__':
    print(get_random_film())

