import random
import os
from gtts import gTTS
from googletrans import Translator
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram import Router, F
from bot_giblets import bot

router = Router()


@router.message(CommandStart(ignore_case=True))
async def handle_start(message: Message):
    await message.answer('Some greeting text here')


@router.message(Command('help', ignore_case=True))
async def handle_help(message: Message):
    await message.answer('В текущей версии я умею:\n'
                         '/start - запуск бота;\n'
                         '/help - справка по командам;\n'
                         '/аудио - пришлю аудиофайл;\n'
                         '/треня - пришлю озувучку случайной тренировки\n'
                         '/перевод "текст" - переведу текст на английский')


@router.message(F.photo)
async def get_photo(message: Message):
    await bot.download(message.photo[-1], destination=f'img/{message.photo[-1].file_id}.jpg')
    await message.answer('Фото сохранено.')


@router.message(Command('аудио'))
async def send_audio(message: Message):
    audio = FSInputFile('audio/zdes-nashi-polnomochiya-vse.mp3')
    await bot.send_audio(message.chat.id, audio)


@router.message(Command('треня'))
async def training(message: Message):
    training_list = [
        "Тренировка 1:\\n1. Скручивания: 3 подхода по 15 повторений\\n2. Велосипед: 3 подхода по 20 повторений (каждая сторона)\\n3. Планка: 3 подхода по 30 секунд",
        "Тренировка 2:\\n1. Подъемы ног: 3 подхода по 15 повторений\\n2. Русский твист: 3 подхода по 20 повторений (каждая сторона)\\n3. Планка с поднятой ногой: 3 подхода по 20 секунд (каждая нога)",
        "Тренировка 3:\\n1. Скручивания с поднятыми ногами: 3 подхода по 15 повторений\\n2. Горизонтальные ножницы: 3 подхода по 20 повторений\\n3. Боковая планка: 3 подхода по 20 секунд (каждая сторона)"
    ]
    await bot.send_chat_action(message.chat.id, 'upload_audio')
    rand_tr = random.choice(training_list)
    audio_workout = gTTS(text=rand_tr, lang='ru')
    audio_workout.save('audio/gtts/workout1.mp3')
    audio = FSInputFile('audio/gtts/workout1.mp3')
    await bot.send_audio(message.chat.id, audio)
    os.remove('audio/gtts/workout1.mp3')


@router.message(Command('перевод'))
async def translate(message: Message, command: CommandObject):
    data = command.args
    if not data:
        await bot.send_message(message.chat.id, 'Пожалуйста введите текст для перевода.')
    else:
        translator = Translator()
        translated = translator.translate(data, dest='en')
        await bot.send_message(message.chat.id, f'{message.from_user.username} says: "{translated.text}"')
