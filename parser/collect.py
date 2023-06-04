from bs4 import BeautifulSoup
import requests
import random
import asyncio
import aiohttp
import re

from utils.db_api import insert_film

re_year_country = re.compile(r'(\d{4}),\s+(.*)')


async def parse_films():
    url = 'https://www.kinoafisha.info/en/rating/movies/'
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            async with session.get(f'{url}?page={i}') as response:
                soup = BeautifulSoup(await response.text(), 'lxml')
                movie_items = soup.findAll('div', 'movieItem_info')
                for item in movie_items:
                    title = item.find('a', 'movieItem_title').text
                    genre = item.find('span', 'movieItem_genres').text
                    try:
                        year, country = re_year_country.search(item.find(
                            'span', 'movieItem_year').text).groups()
                    except:
                        continue
                    await insert_film(title, genre, country, year)


if __name__ == '__main__':
    asyncio.run(parse_films())

