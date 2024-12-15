from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import Message
from keyboards.inline import dynamic_options_keyboard

router = Router()


@router.callback_query(F.data == 'show_more')
async def handle_dynamic(callback: CallbackQuery):
    await callback.message.answer('Вот пара опций на выбор:', reply_markup=dynamic_options_keyboard)


@router.callback_query(F.data == 'option_one')
async def handle_o1(callback: CallbackQuery):
    await callback.message.answer('Вы выбрали опцию №1')


@router.callback_query(F.data == 'option_two')
async def handle_o2(callback: CallbackQuery):
    await callback.message.answer('Вы выбрали опцию №2')
