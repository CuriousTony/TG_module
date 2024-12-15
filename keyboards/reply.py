from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import Message
from aiogram import Router


start_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Привет')],
    [KeyboardButton(text='Пока')]
], resize_keyboard=True, input_field_placeholder='Выбери кнопку...')
