from aiogram import Router, types
from aiogram.filters.command import Command
from utils.db_api import get_random_film

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(await get_random_film())
