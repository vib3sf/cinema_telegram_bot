from bs4 import BeautifulSoup
import requests
import random
import re


def get_random_film(url, tag_title, class_title, pattern=''):
    page = requests.get(url)

    if not page.status_code == 200:
        raise requests.ConnectionError('Something went wrong.')

    soup = BeautifulSoup(page.text, 'html.parser')
    films = soup.findAll(tag_title, class_title)

    if films:
        film = random.choice(films).text
        if pattern:
            match = re.search(pattern, film)
            if film:
                film = match.group(1)
            else:
                raise ValueError("Pattern isn`t found in title.")

        return film


if __name__ == '__main__':
    while True:
        film = get_random_film('https://www.timeout.com/film/best-movies-of-all-time',
                        'h3', '_h3_cuogz_1', pattern=r'\d+\.\s+(.*)')
        print(f'Your film: {film}. Want another?')
        if input() != 'yes':
            break

