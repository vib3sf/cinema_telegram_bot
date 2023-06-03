#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import random
import time 
import sqlite3
import re


re_year_country = re.compile(r'(\d{4}),\s+(.*)')


def collect_films(cursor):
    url = 'https://www.kinoafisha.info/en/rating/movies/'
    for i in range(10):
        page = requests.get(f'{url}?page={i}')

        if not page.status_code == 200:
            raise requests.ConnectionError('Something went wrong.')

        soup = BeautifulSoup(page.text, 'lxml')
        movie_items = soup.findAll('div', 'movieItem_info')
        for item in movie_items:
            title = item.find('a', 'movieItem_title').text
            genre = item.find('span', 'movieItem_genres').text
            try:
                year, country = re_year_country.search(item.find(
                    'span', 'movieItem_year').text).groups()
            except:
                continue
            cursor.execute('INSERT INTO films VALUES (?, ?, ?, ?)', (title, genre, country, year))


if __name__ == '__main__':
    start = time.time()

    with sqlite3.connect('example.db') as connection:
        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS films(
            title TEXT,
            genre TEXT,
            country TEXT,
            year INT
            );
        ''')
        cursor.execute("DELETE FROM films")

        collect_films(cursor)
        connection.commit()

    print(f'Execute time: {time.time() - start}')

