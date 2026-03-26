from aiogram import Router, F
from aiogram.types import Message
from keyboards.xui_main_menu import xui_main_kb

from programs.DeleteClient import delete_client

xui_delete_client_router = Router()

@xui_delete_client_router.message(F.text == "Удалить свой конфиг")
async def handle_hello(message: Message):
    username = message.from_user.username
    delete_client(username)
    await message.answer(
        'Конфиг удален. Можете создать завново в люойй момент',
        reply_markup=xui_main_kb
    )