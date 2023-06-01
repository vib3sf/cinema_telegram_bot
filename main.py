from bs4 import BeautifulSoup
import requests
import random


def get_random_film(films):
    return random.choice(films).text

def main():
    url = 'https://www.kinoafisha.info/rating/movies/'
    page = requests.get(url)

    if not page.status_code == 200:
        print('Something went wrong')
        return 

    soup = BeautifulSoup(page.text, 'html.parser')
    films = soup.findAll('a', 'movieItem_title')

    while True:
        if films:
            film = get_random_film(films)
            print(f'Your film: {film}. Want another?')
            if not input() == 'yes':
                films.remove(film)
                return
        else:
            print('Films are over :(')



if __name__ == '__main__':
    main()

