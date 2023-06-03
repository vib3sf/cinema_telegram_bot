#!/usr/bin/env python
from collect_films import collect_films
from textwrap import dedent
from random import choice


def main():
    print(f'Your film: {choice(collect_films())}.')


if __name__ == '__main__':
    main()

