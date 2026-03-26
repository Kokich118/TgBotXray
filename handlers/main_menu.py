from aiogram import Router, F
from aiogram.types import Message

from keyboards.main_menu import main_kb

main_menu_router = Router()

@main_menu_router.message(F.text == "Назад")
async def handle_hello(message: Message):
    await message.answer(
        "Главное меню",
        reply_markup=main_kb
    )

