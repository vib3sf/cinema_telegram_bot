import os
import asyncio
import aiosqlite
from textwrap import dedent
from random import choice

from config import config


async def insert_film(title: str, genre: str, country: str, year: int):
    async with aiosqlite.connect(config.DB_PATH) as connection:
        await connection.execute('INSERT INTO films VALUES (?, ?, ?, ?)',
                                 (title, genre, country, year))
        await connection.commit()
    

async def collect_films():
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


async def get_random_film() -> str:
    async with aiosqlite.connect(config.DB_PATH) as connection:
        cursor = await connection.cursor()
        await cursor.execute('SELECT title FROM films ORDER BY RANDOM() LIMIT 1;')
        film_fetch = await cursor.fetchone()
    return f'Your film - {film_fetch[0]}'


