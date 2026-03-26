from aiogram import Router, F
from aiogram.types import Message
from keyboards.xui_main_menu import xui_main_kb

xui_server_main_router = Router()

@xui_server_main_router.message(F.text == "VPN через наш сервер")
async def handle_hello(message: Message):
    await message.answer(
        'Перейди в раздел "Посмотреть свой конфиг" чтобы создать, узнать или удалить его. Или "Назад", чтобы вернуться в главное меню',
        reply_markup=xui_main_kb
    )