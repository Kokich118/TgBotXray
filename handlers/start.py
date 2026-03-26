from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.main_menu import main_kb

start_router = Router()

@start_router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать в мир свободного интернета! Есть на выбор 2 варианта: создание vpn через наш сервер или могу помочь настроить vpn с помощью WARP",
        reply_markup=main_kb
    )