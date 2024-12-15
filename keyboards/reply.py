from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

start_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Привет')],
    [KeyboardButton(text='Пока')]
], resize_keyboard=True, input_field_placeholder='Выбери кнопку...')
