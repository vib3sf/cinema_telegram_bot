from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.types import Message, CallbackQuery

from utils.db_api import get_favorites, delete_favorite
from utils.messages import represent_film
from keyboards.remove_favorite import get_remove_keyboard

router = Router()


@router.message(Command('favorites'))
async def show_favorites(message: Message):
    films = await get_favorites(message.from_user.id)
    for film in films:
        await message.answer(
            represent_film(film), 
            reply_markup=get_remove_keyboard(film[0])
        )
    else:
        await message.answer('No favorites :(')


@router.callback_query(lambda c: c.data.startswith('remove_favorite_'))
async def remove_favorite(callback: CallbackQuery):
    await delete_favorite(callback.data.split('_')[-1])

