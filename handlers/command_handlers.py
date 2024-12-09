from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import Router

router = Router()


@router.message(CommandStart(ignore_case=True))
async def handle_start(message: Message):
    await message.answer('Some greeting text here')


@router.message(Command('help', ignore_case=True))
async def handle_help(message: Message):
    await message.answer('Some common info here')
