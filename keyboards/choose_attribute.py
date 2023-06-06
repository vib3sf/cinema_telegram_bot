from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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

