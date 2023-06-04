import os
import asyncio
import aiosqlite
from textwrap import dedent
from random import choice

from config import config
from .representation import represent_film


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
    

async def get_random_film() -> str:
    async with aiosqlite.connect(config.DB_PATH) as connection:
        cursor = await connection.cursor()
        await cursor.execute('SELECT * FROM films ORDER BY RANDOM() LIMIT 1;')
        film_fetch = await cursor.fetchone()
    return await represent_film(film_fetch)


async def get_films_by_genre(genre: str):
    async with aiosqlite.connect(config.DB_PATH) as connection:
        cursor = await connection.cursor()
        await cursor.execute('SELECT * FROM films WHERE genre=?', genre)
        films_fetch = cursor.fetchall()
    return await represent_list_films(films_fetch)


