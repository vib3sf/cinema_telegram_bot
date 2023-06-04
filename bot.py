import argparse
import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import config
from handlers import get_random
from parser.collect import collect_films


async def main():
    bot = Bot(token=config.TOKEN)

    logging.basicConfig(level=logging.INFO)

    dp = Dispatcher()
    dp.include_routers(get_random.router)

    parser = argparse.ArgumentParser(description='Cinema telegram bot')
    parser.add_argument('-r', '--refresh', help='Refresh database', action='store_true')
    args = parser.parse_args()

    if args.refresh:
        await collect_films()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

