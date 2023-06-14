from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_remove_keyboard(film_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Remove', callback_data=f'remove_favorite_{film_id}')]
    ])

