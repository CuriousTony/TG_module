from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

links_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Читать новости', url='https://dzen.ru/')],
    [InlineKeyboardButton(text='Слушать музыку', url='https://music.yandex.ru/')],
    [InlineKeyboardButton(text='Смотреть видео', url='https://ya.ru/video/')]
])

dynamic_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Показать больше', callback_data='show_more')]
])

dynamic_options_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Опция 1', callback_data='option_one')],
    [InlineKeyboardButton(text='Опция 2', callback_data='option_two')]
])
