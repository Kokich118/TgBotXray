from aiogram import Router, F
from aiogram.types import Message
from keyboards.xui_main_menu import xui_main_kb

from programs.AddClient import add_client

xui_add_client_router = Router()

@xui_add_client_router.message(F.text == "Создать свой конфиг")
async def handle_hello(message: Message):
    username = message.from_user.username
    add_client(username)
    await message.answer(
        'Поздравляю! Конфиг создан',
        reply_markup=xui_main_kb
    )