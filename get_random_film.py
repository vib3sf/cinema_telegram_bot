from bs4 import BeautifulSoup
import requests
import random


def get_random_film(url, tag_title, class_title):
    page = requests.get(url)

    if not page.status_code == 200:
        print('Something went wrong')
        return None

    soup = BeautifulSoup(page.text, 'html.parser')
    films = soup.findAll(tag_title, class_title)

    while True:
        if films:
            film = random.choice(films).text
            print(f'Your film: {film}. Want another?')
            if not input() == 'yes':
                films.remove(film)
                return film
        else:
            print('Films are over :(')
            return None


if __name__ == '__main__':
    get_random_film('https://www.kinoafisha.info/rating/movies/', 'a', 'movieItem_title')

