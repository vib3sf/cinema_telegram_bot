from aiogram.types import Message
from aiogram import Router
from aiogram.filters import Command, Text

from utils.messages import start_message

router = Router()


@router.message(Command('start'))
async def start(message: Message):
    await message.answer(start_message())

