from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
)

attribute_buttons = (
    "Any attribute", "Genre", "Country", "Year"
)

def get_attribute_keyboard():
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
        input_field_placeholder="Choose a attribute"
    )

def try_again_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
        InlineKeyboardButton(text='Try again', callback_data='try_again'),
        InlineKeyboardButton(text='Another attribute', callback_data='change_attribute')
        ]
    ])

