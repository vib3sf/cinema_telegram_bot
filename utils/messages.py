from textwrap import dedent


def start_message() -> str:
    return dedent('''
                  Welcome to the Cinema Bot.
                  There you can get random film by genre, year, country and many more.
                  To get film type /random.
                  ''')

def represent_film(film_fetch: tuple) -> str:
    return dedent(f'''
                  Title film: {film_fetch[1]}
                  Genre: {film_fetch[2]}
                  Country: {film_fetch[3]}
                  Year: {film_fetch[4]}
                  ''') if film_fetch else 'Film is not found :('

