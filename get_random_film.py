from collect_films import collect_films
from textwrap import dedent
from random import choice
import sqlite3


def get_random_film():
    connection = sqlite3.connect('films.db')
    cur = connection.cursor()
    cur.execute('SELECT title FROM films ORDER BY RANDOM() LIMIT 1;')
    film = cur.fetchone()[0]
    connection.close()
    return f'Your film - {film}'


if __name__ == '__main__':
    print(get_random_film())

