from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.main_menu import main_kb

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать 👋",
        reply_markup=main_kb
    )