from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext

from keyboards.choose_attribute import (
    get_attribute_keyboard, attribute_buttons, try_again_keyboard)
from utils.db_api import get_random_film

router = Router()


class FormState(StatesGroup):
    choosing_attribute = State()
    inputing_search_text = State()
    skip_inputing = State()


@router.message(Command('random'))
async def start_search_random(message: Message, state: FSMContext):
    await message.answer(
        text='Choose film attribute for searching.', 
        reply_markup=get_attribute_keyboard()
    )
    await state.set_state(FormState.choosing_attribute)


@router.message(FormState.choosing_attribute, F.text.in_(attribute_buttons))
async def get_search_input(message: Message, state: FSMContext):
    selected_attribute = message.text.lower()
    await state.update_data(selected_attribute=selected_attribute)

    if selected_attribute == 'any attribute':
        await state.set_state(FormState.skip_inputing)
        await send_search_result(message, state)
    else:
        await message.answer(
            text=f'Input the {selected_attribute}.'
        )

        await state.set_state(FormState.inputing_search_text)


@router.message(FormState.choosing_attribute)
async def wrong_input(message: Message):
    await message.answer(
        text='Wrong attribute.',
        reply_markup=get_attribute_keyboard(),
    )


@router.message(FormState.inputing_search_text)
@router.message(FormState.skip_inputing)
async def send_search_result(message: Message, state: FSMContext):
    user_data = await state.get_data()
    user_input = message.text.lower() if 'user_input' not in user_data else user_data['user_input']
    await state.update_data(user_input=user_input)
    selected_attribute = user_data['selected_attribute']

    film = await get_random_film() if selected_attribute == 'any attribute' else \
        await get_random_film((selected_attribute, user_input))

    await message.answer(film, reply_markup=try_again_keyboard())
    await state.set_state(FormState.choosing_attribute)


@router.callback_query(Text("try_again"))
async def try_again(callback: CallbackQuery, state: FSMContext):
    await send_search_result(callback.message, state)

@router.callback_query(Text('change_attribute'))
async def change_attribute(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await start_search_random(callback.message, state)


    
    

