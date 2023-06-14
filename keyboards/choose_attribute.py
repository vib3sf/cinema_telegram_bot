from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

attribute_buttons = (
    "Any attribute", "Genre", "Country", "Year"
)

def get_attribute_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=
        [
            [
                KeyboardButton(text=attribute_buttons[0])
            ],
            [
                KeyboardButton(text=attribute_buttons[1]),
                KeyboardButton(text=attribute_buttons[2]),
                KeyboardButton(text=attribute_buttons[3]),
            ],
        ],
        input_field_placeholder="Choose a attribute",
        resize_keyboard=True,
    )

def try_again_keyboard(is_found: bool = True) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text='Another attribute', callback_data='change_attribute'))
    if is_found:
        builder.add(InlineKeyboardButton(
            text='Try again', callback_data='try_again'
        ))
        builder.row(InlineKeyboardButton(
            text='Add to favorites', callback_data='add_favorite'
        ))

    return builder.as_markup()

