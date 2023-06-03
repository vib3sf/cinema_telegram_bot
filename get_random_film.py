#!/usr/bin/env python
from collect_films import collect_films
from textwrap import dedent
from random import choice


def get_random_film():
    return f'Ваш фильм: {choice(collect_films())}'


if __name__ == '__main__':
    print(get_random_film())

