#!/usr/bin/env python
from get_random_film import get_random_film
from textwrap import dedent


def main():
    while True:
        print(dedent('''\
            Select the size we need to get a random film from:
            1) kinoafisha.info 
            2) timeout.com
            3) rollingstone.com'''
        ))
        n_site = input('Your choice: ')
        match n_site:
            case '1':
                film = get_random_film('https://www.kinoafisha.info/rating/movies/', 
                                       'a', 'movieItem_title')
            case '2':
                film = get_random_film('https://www.timeout.com/film/best-movies-of-all-time',
                                       'h3', '_h3_cuogz_1', pattern=r'\d+\.\s+(.*)')
            case '3':
                film = get_random_film('https://au.rollingstone.com/100-greatest-movies-of-all-time/page/1/kill-bill-volume-1/',
                                       'h3', 'c-list__title t-bold')
            case _:
                print('Wrong input. Try again.')
                continue
        break
    print(f'Your film: {film}.')


if __name__ == '__main__':
    main()

