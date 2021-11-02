from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from  filters import IsGroup

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name} siz guruhdasiz!")



@dp.message_handler(CommandStart(),IsGroup())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name} siz guruhdasiz!")
