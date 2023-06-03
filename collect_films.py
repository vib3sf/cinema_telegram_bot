from bs4 import BeautifulSoup
import requests
import random
import time 


def collect_films():
    url = 'https://www.kinoafisha.info/rating/movies/'
    films = []
    for i in range(10):
        page = requests.get(f'{url}?page={i}')

        if not page.status_code == 200:
            raise requests.ConnectionError('Something went wrong.')

        soup = BeautifulSoup(page.text, 'html.parser')
        films += [film.text for film in soup.findAll('a', 'movieItem_title')]

    return films


if __name__ == '__main__':
    start = time.time()
    print(f'Your film: {random.choice(collect_films())}')
    end = time.time()
    print(f"Execution time is {end - start:.2f} sec.")

