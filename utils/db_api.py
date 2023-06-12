import os
import asyncio
import aiosqlite
from textwrap import dedent
from random import choice

from config import config
from .messages import represent_film


async def refresh_table():
    async with aiosqlite.connect(config.DB_PATH) as connection:

        await connection.execute('''CREATE TABLE IF NOT EXISTS films(
            title TEXT,
            genre TEXT,
            country TEXT,
            year INT
            );
        ''')
        await connection.execute("DELETE FROM films")

        await connection.commit()



async def insert_film(title: str, genre: str, country: str, year: int):
    async with aiosqlite.connect(config.DB_PATH) as connection:
        await connection.execute('INSERT INTO films VALUES (?, ?, ?, ?)',
                                 (title, genre, country, year))
        await connection.commit()
    

# tuple is condition of search from db, where first element is row and second is condition
# if empty_tuple -> search from all films

async def get_random_film(row_condition: tuple = ()) -> dict:
    if len(row_condition) not in (0, 2):
        raise ValueError("Argument must only have two elements.")
    
    if row_condition and row_condition[0] not in ('title', 'genre', 'country', 'year'):
        raise ValueError('Row is not exist in films table.')


    if row_condition:
        if row_condition[0] in ('genre', 'country'):
            condition = f"WHERE LOWER({row_condition[0]}) LIKE '%{row_condition[1]}%'"
        elif row_condition[0] == 'year':
            if not row_condition[1].isdigit():
                return {'text': 'Year cannot contains letters', 'is_found': False}

            condition = f'WHERE {row_condition[0]}={row_condition[1]}'
    else: 
        condition = ''

    async with aiosqlite.connect(config.DB_PATH) as connection:
        cursor = await connection.cursor()
        await cursor.execute(f'SELECT * FROM films {condition} ORDER BY RANDOM() LIMIT 1;')

        film_fetch = await cursor.fetchone()
    return {'text': represent_film(film_fetch), 'is_found': bool(film_fetch)}


