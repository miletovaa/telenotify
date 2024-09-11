from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Hello! Вас не слышно! Я вас не вижу!")
