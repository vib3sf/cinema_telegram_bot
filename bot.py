import argparse
import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import config
from handlers import get_random, start
from parser.collect import collect_films
from utils.db_api import create_tables, refresh_all_tables, refresh_films, refresh_favorites


async def main():
    bot = Bot(token=config.TOKEN)

    logging.basicConfig(level=logging.INFO)

    dp = Dispatcher()
    dp.include_routers(start.router, get_random.router)

    parser = argparse.ArgumentParser(description='Cinema telegram bot')

    parser.add_argument('-f', '--refreshfilms', help='Refresh films table', 
                        action='store_true')
    parser.add_argument('-u', '--refreshfavorites', help='Refresh favorites table', 
                        action='store_true')
    parser.add_argument('-a', '--refreshall', help='Create or refresh all tables', 
                        action='store_true')

    args = parser.parse_args()
    await create_tables()

    if args.refreshall:
        await refresh_all_tables()
    elif args.refreshfilms:
        await collect_films()
    elif args.refreshfavorites:
        await refresh_favorites()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

