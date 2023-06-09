from textwrap import dedent

def represent_film(film_fetch: tuple) -> str:
    return dedent(f'''
                  Title film: {film_fetch[0]}
                  Genre: {film_fetch[1]}
                  Country: {film_fetch[2]}
                  Year: {film_fetch[3]}
                  ''') if film_fetch else 'Film is not found :('


def represent_list_films(films_fetch: list) -> str:
    return '\n\n'.join([represent_film(film_fetch) for film_fetch in films_fetch])

