from textwrap import dedent

async def represent_film(film_fetch: tuple) -> str:
    return dedent(f'''
                  Title film: {film_fetch[0]}
                  Genre: {film_fetch[1]}
                  Country: {film_fetch[2]}
                  Year: {film_fetch[3]}
                  ''')


async def represent_list_films(films_fetch: list) -> str:
    return '\n\n'.join([represent_film(film_fetch) for film_fetch in films_fetch])

