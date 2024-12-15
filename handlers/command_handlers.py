import random
import os
import sqlite3
from aiogram.fsm.context import FSMContext
from gtts import gTTS
from googletrans import Translator
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram import Router, F
from bot_giblets import bot
from table.db_form import FormDB

router = Router()


@router.message(CommandStart(ignore_case=True))
async def handle_start(message: Message, state: FSMContext):
    await message.answer('Привет, я Зеробот!\nА как зовут тебя?')
    await state.set_state(FormDB.name)


@router.message(FormDB.name)
async def name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Сколько тебе лет?')
    await state.set_state(FormDB.age)


@router.message(FormDB.age)
async def age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('В каком ты классе?')
    await state.set_state(FormDB.grade)


@router.message(FormDB.grade)
async def grade(message: Message, state: FSMContext):
    await state.update_data(grade=message.text)
    student_data = await state.get_data()
    conn = sqlite3.connect('school_data.db')
    curs = conn.cursor()
    curs.execute('''INSERT INTO students(name, age, grade) VALUES (?, ?, ?)''',
                 (student_data['name'], student_data['age'], student_data['grade'])
                 )
    await message.answer(f'Отлично! Твое имя {student_data['name']}, тебе {student_data['age']} лет\n'
                         f'и ты учишься в {student_data['grade']} классе!\n'
                         f'Приятно познакомиться, {student_data['name']}!')
    conn.commit()
    conn.close()


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
