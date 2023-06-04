from aiogram import Router, types
from aiogram.filters.command import Command
from utils.db_api import get_random_film
from parser.collect import parse_films

router = Router()

@router.message(Command("refresh"))
async def cmd_start(message: types.Message):
    await parse_films()
